# MailBot — SMTP Email CLI

A small Python command-line tool for sending one UTF-8 plain-text email through a configured SMTP provider.

> **Status:** modernized academic portfolio project. Suitable for learning, local automation, and controlled experiments; not intended for bulk email or production-critical delivery.

## 日本語概要

MailBot は、SMTP を使用して UTF-8 のプレーンテキストメールを1通送信する Python CLI ツールです。

環境変数による認証情報の管理、Gmail・Outlook・Yahoo! JAPAN の設定プリセット、送信前の入力検証、SMTP をモック化した自動テストを含みます。大量配信サービスや本番向け通知基盤ではありません。

## Features

- Gmail, Outlook, Yahoo! JAPAN, and custom SMTP configuration;
- STARTTLS and direct SSL transport modes;
- UTF-8 subjects and bodies, including Japanese and Portuguese;
- credentials loaded from environment variables;
- CLI arguments with `.env` defaults;
- dry-run preview without an SMTP connection;
- validation against malformed addresses and header injection;
- automated tests that never send real email;
- predictable exit codes for scripts and scheduled tasks.

## Requirements

- Python 3.10+
- an SMTP account or relay;
- an app password or provider-specific SMTP credential when required.

## Installation

```bash
git clone https://github.com/artloock/MailBot.git
cd MailBot
python -m venv .venv
```

Activate the environment on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install the dependency:

```bash
python -m pip install -r requirements.txt
```

## Configuration

Copy `.env.example` to `.env` and replace the placeholder values:

```dotenv
SMTP_PROVIDER=gmail
SMTP_USER=sender@example.com
SMTP_PASSWORD=replace-with-app-password
MAIL_FROM=sender@example.com
```

Never commit `.env`. It is ignored by Git, but production credentials should preferably be stored in a dedicated secret manager.

## Usage

Preview and validate a message without connecting to SMTP:

```bash
python -m src.mailbot \
  --to recipient@example.com \
  --subject "通知テスト" \
  --body "こんにちは。Este é um teste." \
  --dry-run
```

Send using Gmail and values from `.env`:

```bash
python -m src.mailbot \
  --provider gmail \
  --to recipient@example.com \
  --subject "Notification" \
  --body "The scheduled task completed."
```

PowerShell uses the backtick for multiline commands:

```powershell
python -m src.mailbot `
  --provider outlook `
  --to recipient@example.com `
  --subject "Test" `
  --body "Message body"
```

## Providers

| Provider | Host | Port | Security |
|---|---|---:|---|
| Gmail | `smtp.gmail.com` | 587 | STARTTLS |
| Outlook | `smtp.office365.com` | 587 | STARTTLS |
| Yahoo! JAPAN | `smtp.mail.yahoo.co.jp` | 465 | SSL |
| Custom | environment-defined | environment-defined | configurable |

Provider policies change. Confirm SMTP access and authentication requirements in the provider's current documentation before use.

## Exit Codes

| Code | Meaning |
|---:|---|
| `0` | Message validated or delivered successfully |
| `1` | SMTP connection or delivery failed |
| `2` | Configuration or input validation failed |

## Tests

```bash
python -m unittest discover -s tests -v
```

The SMTP client is mocked during tests. Running the test suite does not send email.

## Project Structure

```text
MailBot/
├── src/
│   ├── config.py
│   └── mailbot.py
├── tests/
│   ├── test_config.py
│   └── test_mailbot.py
├── docs/
│   └── architecture.md
├── .env.example
└── requirements.txt
```

See [Architecture](docs/architecture.md) for design decisions and security boundaries.

## Limitations

- plain-text messages only;
- one recipient and one message per execution;
- no attachments, HTML templates, queue, retries, rate limiting, or delivery tracking;
- `.env` is convenient for local development but is not a full secret-management solution;
- compliance with organizational or legal requirements depends on deployment, policy, and operation—not merely on this script.

## License and Attribution

Released under the [MIT License](LICENSE). Copies or substantial portions must retain the original copyright and license notice.

## Author

**Arthur Alves Stefanini**
[LinkedIn](https://www.linkedin.com/in/arthur-alves-stefanini-973a99169/)
