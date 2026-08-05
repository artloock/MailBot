# Architecture

## Scope

MailBot is a small command-line SMTP client for sending one UTF-8 plain-text message at a time. It is a portfolio and learning project, not a bulk-mail platform, queue processor, or corporate notification service.

## Components

### `src/config.py`

- defines SMTP provider presets;
- reads credentials and overrides from environment variables;
- validates ports, timeouts, and transport security;
- keeps secrets outside the repository.

### `src/mailbot.py`

- parses CLI arguments;
- validates recipient, subject, and body;
- builds a UTF-8 `EmailMessage`;
- selects SMTP, STARTTLS, or SMTP-over-SSL;
- returns predictable process exit codes.

### `tests/`

- validates provider configuration;
- checks Japanese and Portuguese UTF-8 content;
- tests header-injection rejection;
- mocks SMTP so automated tests never send real email.

## Security Boundaries

- `.env` reduces accidental credential commits but is not a secret manager.
- TLS protects transport when configured correctly; it does not guarantee recipient identity or message confidentiality after delivery.
- Provider app passwords or dedicated SMTP credentials are preferred over primary account passwords.
- Bulk delivery, retry queues, rate limiting, audit logging, and compliance controls are outside the current scope.

## Data Flow

1. `.env` and CLI arguments provide configuration and message content.
2. Input is validated before any connection is opened.
3. The message is encoded as UTF-8.
4. The selected SMTP transport authenticates and sends the message.
5. The process returns `0`, `1`, or `2` for automation-friendly handling.
