# MailBot (EN/JA) | Secure Email Automation for Corporate Use

**EN:** MailBot is a lightweight Python email-sending utility designed for corporate-friendly automation: simple configuration, secure secret handling, and predictable outputs.  
**JA:** MailBot は、企業利用を想定した軽量のメール送信ツールです。設定が簡単で、秘密情報を安全に扱い、安定した出力を提供します。

---

## Key Features / 主な機能
- **Secure secrets** via `.env` (no passwords hardcoded) / `.env` により秘密情報を安全に管理
- **UTF-8 ready** (Japanese content support) / UTF-8 対応（日本語本文OK）
- **SMTP compatible** (Gmail, Outlook, Yahoo, corporate SMTP) / 各種SMTP対応（Gmail/Outlook/社内SMTP等）
- **Clean structure** (`src/`, `docs/`, `tests/`) / 構成が明確（src/docs/tests）

---

## Quick Start / クイックスタート

### 1) Install / インストール
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
# source .venv/bin/activate

pip install -r requirements.txt