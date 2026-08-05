"""Command-line SMTP email sender with UTF-8 message support."""

from __future__ import annotations

import argparse
import os
import smtplib
import ssl
import sys
from email.message import EmailMessage
from email.utils import parseaddr

from src.config import ConfigurationError, SmtpConfig


def validate_email_address(value: str) -> str:
    """Return a normalized address or raise a user-facing validation error."""
    _, address = parseaddr(value)
    if not address or "@" not in address or "\n" in value or "\r" in value:
        raise ValueError(f"Invalid email address: {value!r}")
    return address


def build_message(sender: str, recipient: str, subject: str, body: str) -> EmailMessage:
    """Create a UTF-8 plain-text email message."""
    if not subject.strip():
        raise ValueError("Subject cannot be empty.")
    if "\n" in subject or "\r" in subject:
        raise ValueError("Subject cannot contain line breaks.")
    if not body.strip():
        raise ValueError("Body cannot be empty.")

    message = EmailMessage()
    message["From"] = validate_email_address(sender)
    message["To"] = validate_email_address(recipient)
    message["Subject"] = subject
    message.set_content(body, charset="utf-8")
    return message


def send_message(config: SmtpConfig, message: EmailMessage) -> None:
    """Send one message using the configured SMTP transport."""
    tls_context = ssl.create_default_context()

    if config.security == "ssl":
        with smtplib.SMTP_SSL(
            config.host,
            config.port,
            timeout=config.timeout,
            context=tls_context,
        ) as client:
            client.login(config.username, config.password)
            client.send_message(message)
        return

    with smtplib.SMTP(config.host, config.port, timeout=config.timeout) as client:
        client.ehlo()
        if config.security == "starttls":
            client.starttls(context=tls_context)
            client.ehlo()
        client.login(config.username, config.password)
        client.send_message(message)


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Send one UTF-8 plain-text email through an SMTP server."
    )
    parser.add_argument(
        "--provider",
        choices=("gmail", "outlook", "yahoo_jp", "custom"),
        default=os.getenv("SMTP_PROVIDER", "gmail"),
        help="SMTP preset. Custom uses SMTP_HOST, SMTP_PORT, and SMTP_SECURITY.",
    )
    parser.add_argument("--to", dest="recipient", default=os.getenv("MAIL_TO"))
    parser.add_argument("--subject", default=os.getenv("MAIL_SUBJECT"))
    parser.add_argument("--body", default=os.getenv("MAIL_BODY"))
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate and preview the message without connecting to SMTP.",
    )
    return parser


def configure_console_encoding() -> None:
    """Prefer UTF-8 for multilingual output on supported terminals."""
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure:
            reconfigure(encoding="utf-8", errors="replace")


def main(argv: list[str] | None = None) -> int:
    try:
        from dotenv import load_dotenv

        configure_console_encoding()
        load_dotenv()
        args = create_parser().parse_args(argv)

        if not args.recipient:
            raise ValueError("Recipient is required via --to or MAIL_TO.")
        if not args.subject:
            raise ValueError("Subject is required via --subject or MAIL_SUBJECT.")
        if not args.body:
            raise ValueError("Body is required via --body or MAIL_BODY.")

        if args.dry_run:
            sender = os.getenv("MAIL_FROM", "preview@example.invalid")
            message = build_message(sender, args.recipient, args.subject, args.body)
            print("Dry run: message validated; no SMTP connection was made.")
            print(message)
            return 0

        config = SmtpConfig.from_environment(args.provider)
        message = build_message(
            config.sender,
            args.recipient,
            args.subject,
            args.body,
        )
        send_message(config, message)
        print(f"Email sent successfully to {args.recipient}.")
        return 0
    except (ConfigurationError, ValueError) as exc:
        print(f"Configuration error: {exc}", file=sys.stderr)
        return 2
    except (OSError, smtplib.SMTPException) as exc:
        print(f"Delivery failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
