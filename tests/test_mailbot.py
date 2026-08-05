import unittest
from unittest.mock import MagicMock, patch

from src.config import SmtpConfig
from src.mailbot import build_message, send_message


class MessageTests(unittest.TestCase):
    def test_build_message_preserves_utf8_content(self):
        message = build_message(
            "sender@example.com",
            "recipient@example.com",
            "通知テスト",
            "こんにちは。Este é um teste.",
        )

        self.assertEqual(message["Subject"], "通知テスト")
        self.assertIn("こんにちは", message.get_content())

    def test_subject_rejects_header_injection(self):
        with self.assertRaises(ValueError):
            build_message(
                "sender@example.com",
                "recipient@example.com",
                "Valid\nBcc: attacker@example.com",
                "Body",
            )

    @patch("src.mailbot.smtplib.SMTP")
    def test_starttls_delivery_uses_login_and_send_message(self, smtp_class):
        client = MagicMock()
        smtp_class.return_value.__enter__.return_value = client
        config = SmtpConfig(
            host="smtp.example.com",
            port=587,
            username="sender@example.com",
            password="secret",
            sender="sender@example.com",
            security="starttls",
        )
        message = build_message(
            config.sender,
            "recipient@example.com",
            "Test",
            "Body",
        )

        send_message(config, message)

        client.starttls.assert_called_once()
        client.login.assert_called_once_with(config.username, config.password)
        client.send_message.assert_called_once_with(message)


if __name__ == "__main__":
    unittest.main()
