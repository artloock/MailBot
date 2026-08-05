"""SMTP configuration loaded from environment variables."""

from __future__ import annotations

import os
from dataclasses import dataclass


class ConfigurationError(ValueError):
    """Raised when required SMTP configuration is missing or invalid."""


@dataclass(frozen=True)
class ProviderPreset:
    host: str
    port: int
    security: str


PROVIDER_PRESETS = {
    "gmail": ProviderPreset("smtp.gmail.com", 587, "starttls"),
    "outlook": ProviderPreset("smtp.office365.com", 587, "starttls"),
    "yahoo_jp": ProviderPreset("smtp.mail.yahoo.co.jp", 465, "ssl"),
}


@dataclass(frozen=True)
class SmtpConfig:
    host: str
    port: int
    username: str
    password: str
    sender: str
    security: str = "starttls"
    timeout: float = 15.0

    @classmethod
    def from_environment(cls, provider: str = "gmail") -> "SmtpConfig":
        """Build validated SMTP settings from environment variables."""
        preset = PROVIDER_PRESETS.get(provider)
        if preset is None and provider != "custom":
            choices = ", ".join((*PROVIDER_PRESETS, "custom"))
            raise ConfigurationError(
                f"Unknown provider '{provider}'. Choose one of: {choices}."
            )

        host = os.getenv("SMTP_HOST") or (preset.host if preset else "")
        port_text = os.getenv("SMTP_PORT") or str(preset.port if preset else "")
        security = (
            os.getenv("SMTP_SECURITY") or (preset.security if preset else "starttls")
        ).lower()
        username = os.getenv("SMTP_USER", "")
        password = os.getenv("SMTP_PASSWORD", "")
        sender = os.getenv("MAIL_FROM") or username
        timeout_text = os.getenv("SMTP_TIMEOUT", "15")

        missing = [
            name
            for name, value in {
                "SMTP_HOST": host,
                "SMTP_PORT": port_text,
                "SMTP_USER": username,
                "SMTP_PASSWORD": password,
                "MAIL_FROM or SMTP_USER": sender,
            }.items()
            if not value
        ]
        if missing:
            raise ConfigurationError(
                "Missing required configuration: " + ", ".join(missing)
            )

        try:
            port = int(port_text)
        except ValueError as exc:
            raise ConfigurationError("SMTP_PORT must be an integer.") from exc

        try:
            timeout = float(timeout_text)
        except ValueError as exc:
            raise ConfigurationError("SMTP_TIMEOUT must be numeric.") from exc

        if not 1 <= port <= 65535:
            raise ConfigurationError("SMTP_PORT must be between 1 and 65535.")
        if timeout <= 0:
            raise ConfigurationError("SMTP_TIMEOUT must be greater than zero.")
        if security not in {"starttls", "ssl", "none"}:
            raise ConfigurationError(
                "SMTP_SECURITY must be one of: starttls, ssl, none."
            )

        return cls(
            host=host,
            port=port,
            username=username,
            password=password,
            sender=sender,
            security=security,
            timeout=timeout,
        )
