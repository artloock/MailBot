MailBot (EN/JA) | Secure Email Automation for Corporate Use
EN: MailBot is a lightweight Python email-sending utility designed for corporate-friendly automation: simple configuration, secure secret handling, and predictable outputs.
JA: MailBot は、企業利用を想定した軽量のメール送信ツールです。設定が簡単で、秘密情報を安全に扱い、安定した出力を提供します。
Key Features / 主な機能
• Secure secrets via .env (no passwords hardcoded) / .env により秘密情報を安全に管理
• UTF‑8 ready (Japanese content support) / UTF‑8 対応（日本語本文OK）
• SMTP compatible (Gmail, Outlook, Yahoo, corporate SMTP) / 各種SMTP対応（Gmail/Outlook/社内SMTP等）
• Clean structure (src/, docs/, tests/) / 構成が明確（src/docs/tests）
Quick Start / クイックスタート
1) Install / インストール
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
# source .venv/bin/activate

pip install -r requirements.txt
2) Configure .env / 設定（.env）
Create a .env file in the project root:
SMTP_HOST=smtp.example.com
SMTP_PORT=587
SMTP_USER=your_user
SMTP_PASS=your_password
SMTP_USE_TLS=true

MAIL_FROM=your_user@example.com
MAIL_TO=recipient@example.com
MAIL_SUBJECT=Hello / こんにちは
MAIL_BODY=This is a test message. / テストメッセージです。
3) Run / 実行
python -m src.mailbot
Corporate Notes / 企業利用メモ
EN: For corporate environments, prefer App Passwords or SMTP relay accounts and keep credentials outside the codebase.
JA: 企業環境では、アプリパスワードやSMTPリレーアカウントの利用を推奨します。認証情報はコードに含めず、外部で管理してください。
Roadmap / 今後の予定
• CLI flags: --to, --subject, --body, --lang en|ja / CLIオプション追加
• Timezone support (JST) for logs / ログのJST対応
• Better logging (e.g., request IDs, exit codes) / 監査向けログ強化（ID/終了コード）
License
MIT
Author
Arthur Alves Stefanini
LinkedIn: https://www.linkedin.com/in/arthur-alves-stefanini-973a99169/