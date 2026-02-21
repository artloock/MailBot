# Project Architecture (Architecture Design)

## Overview
The MailBot system is designed with a focus on **Security** and **Modularity**. 
This project uses a "Separation of Concerns" approach to make it professional and enterprise-ready.



---

## 1. Environment Variables (.env)
**Role:** Security and Privacy.

* **Purpose:** Stores sensitive data like email addresses and passwords.
* **Security:** This file is listed in `.gitignore`. It is never uploaded to GitHub.
* **Market Standard:** This follows the best practices for security (APPI compliance in Japan).

## 2. Configuration File (config.py)
**Role:** Centralized Management.

* **Purpose:** Stores all SMTP server settings (Gmail, Outlook, Yahoo JP) in one place.
* **Scalability:** To add a new email provider, you only update this file. You do not need to change the main logic.
* **Efficiency:** Centralizing constants makes the code cleaner and easier to maintain.

## 3. Source Code (src/Email-prompt.py)
**Role:** Core Logic.

* **Function:** The main script imports settings from `config.py` and secrets from `.env`.
* **Internationalization:** Uses UTF-8 encoding to support Japanese characters (Kanji/Kana) without errors.