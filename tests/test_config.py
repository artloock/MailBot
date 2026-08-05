import os
import unittest
from unittest.mock import patch

from src.config import ConfigurationError, SmtpConfig


class SmtpConfigTests(unittest.TestCase):
    def test_gmail_preset_uses_environment_credentials(self):
        environment = {
            "SMTP_USER": "sender@example.com",
            "SMTP_PASSWORD": "app-password",
        }
        with patch.dict(os.environ, environment, clear=True):
            config = SmtpConfig.from_environment("gmail")

        self.assertEqual(config.host, "smtp.gmail.com")
        self.assertEqual(config.port, 587)
        self.assertEqual(config.security, "starttls")
        self.assertEqual(config.sender, "sender@example.com")

    def test_yahoo_jp_preset_uses_direct_ssl(self):
        environment = {
            "SMTP_USER": "sender@example.com",
            "SMTP_PASSWORD": "app-password",
        }
        with patch.dict(os.environ, environment, clear=True):
            config = SmtpConfig.from_environment("yahoo_jp")

        self.assertEqual(config.port, 465)
        self.assertEqual(config.security, "ssl")

    def test_missing_credentials_raise_configuration_error(self):
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaises(ConfigurationError):
                SmtpConfig.from_environment("gmail")


if __name__ == "__main__":
    unittest.main()
