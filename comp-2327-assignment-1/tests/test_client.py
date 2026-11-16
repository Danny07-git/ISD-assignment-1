"""Tests for Client."""

import unittest
from types import SimpleNamespace
from unittest.mock import patch

from email_validator import EmailNotValidError

from account.client import Client


class TestClient(unittest.TestCase):
    def setUp(self):
        self.client = Client(1010, "Pete Zahut", "pzahut@example.ca")

    def test_init_rejects_negative_id(self):
        with self.assertRaisesRegex(ValueError, "^client_id must be a value greater than zero$"):
            Client(-1, "Pete", "pete@example.ca")

    def test_init_rejects_zero_id(self):
        with self.assertRaisesRegex(ValueError, "^client_id must be a value greater than zero$"):
            Client(0, "Pete", "pete@example.ca")

    def test_init_rejects_blank_name_after_trimming(self):
        with self.assertRaisesRegex(ValueError, "^name cannot be an empty string$"):
            Client(1, "   ", "pete@example.ca")

    def test_init_rejects_invalid_email(self):
        with patch("account.client.validate_email", side_effect=EmailNotValidError("bad email")):
            with self.assertRaises(EmailNotValidError):
                Client(1, "Pete", "invalid")

    def test_init_sets_trimmed_and_normalized_values(self):
        with patch("account.client.validate_email", return_value=SimpleNamespace(normalized="pete@example.ca")) as validate:
            client = Client(7, " Pete Zahut ", " pete@example.ca ")
        self.assertEqual(client._Client__client_id, 7)
        self.assertEqual(client._Client__name, "Pete Zahut")
        self.assertEqual(client._Client__email_address, "pete@example.ca")
        validate.assert_called_once_with("pete@example.ca", check_deliverability=False)

    def test_client_id_property_returns_current_state(self):
        self.assertEqual(self.client.client_id, 1010)

    def test_name_property_returns_current_state(self):
        self.assertEqual(self.client.name, "Pete Zahut")

    def test_email_property_returns_current_state(self):
        self.assertEqual(self.client.email_address, "pzahut@example.ca")

    def test_email_setter_rejects_invalid_value(self):
        with patch("account.client.validate_email", side_effect=EmailNotValidError("bad email")):
            with self.assertRaises(EmailNotValidError):
                self.client.email_address = "invalid"

    def test_email_setter_stores_normalized_value(self):
        with patch("account.client.validate_email", return_value=SimpleNamespace(normalized="new@example.ca")) as validate:
            self.client.email_address = " new@example.ca "
        self.assertEqual(self.client._Client__email_address, "new@example.ca")
        validate.assert_called_once_with("new@example.ca", check_deliverability=False)

    def test_str_returns_formatted_client(self):
        self.assertEqual(str(self.client), "Pete Zahut [1010] - pzahut@example.ca")


if __name__ == "__main__":
    unittest.main()
