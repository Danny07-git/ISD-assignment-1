"""Tests for BankAccount."""

import unittest
from unittest.mock import patch

from account.account_status import AccountStatus
from account.bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(20019, 100.00, "Alex", AccountStatus.ACTIVE)

    def test_init_rejects_negative_id(self):
        with self.assertRaisesRegex(ValueError, "^account_id must be a value greater than zero$"):
            BankAccount(-1, 0, "Alex", AccountStatus.ACTIVE)

    def test_init_rejects_zero_id(self):
        with self.assertRaisesRegex(ValueError, "^account_id must be a value greater than zero$"):
            BankAccount(0, 0, "Alex", AccountStatus.ACTIVE)

    def test_init_sets_attributes(self):
        self.assertEqual(self.account._BankAccount__account_id, 20019)
        self.assertEqual(self.account._BankAccount__balance, 100.00)
        self.assertEqual(self.account._BankAccount__owner, "Alex")
        self.assertIs(self.account._BankAccount__status, AccountStatus.ACTIVE)

    def test_account_id_property_returns_current_state(self):
        self.assertEqual(self.account.account_id, 20019)

    def test_balance_property_returns_current_state(self):
        self.assertEqual(self.account.balance, 100.00)

    def test_owner_property_returns_current_state(self):
        self.assertEqual(self.account.owner, "Alex")

    def test_status_property_returns_current_state(self):
        self.assertIs(self.account.status, AccountStatus.ACTIVE)

    def test_update_balance_increases_balance(self):
        self.account.update_balance(12.50)
        self.assertEqual(self.account._BankAccount__balance, 112.50)

    def test_update_balance_decreases_balance(self):
        self.account.update_balance(-12.50)
        self.assertEqual(self.account._BankAccount__balance, 87.50)

    def test_deposit_rejects_negative_amount(self):
        with patch.object(self.account, "update_balance") as update:
            with self.assertRaisesRegex(ValueError, "^amount must be a value greater than or equal to zero$"):
                self.account.deposit(-1)
            update.assert_not_called()

    def test_deposit_updates_balance(self):
        with patch.object(self.account, "update_balance") as update:
            self.account.deposit(25)
            update.assert_called_once_with(25)

    def test_withdraw_rejects_negative_amount(self):
        with patch.object(self.account, "update_balance") as update:
            with self.assertRaisesRegex(ValueError, "^amount must be a value greater than or equal to zero$"):
                self.account.withdraw(-1)
            update.assert_not_called()

    def test_withdraw_accepts_zero(self):
        with patch.object(self.account, "update_balance") as update:
            self.account.withdraw(0)
            update.assert_called_once_with(0)

    def test_withdraw_rejects_amount_greater_than_balance(self):
        with patch.object(self.account, "update_balance") as update:
            with self.assertRaisesRegex(ValueError, "^amount cannot exceed the account balance$"):
                self.account.withdraw(101)
            update.assert_not_called()

    def test_withdraw_subtracts_amount(self):
        with patch.object(self.account, "update_balance") as update:
            self.account.withdraw(20)
            update.assert_called_once_with(-20)

    def test_str_returns_formatted_account(self):
        self.assertEqual(str(self.account), "Account Number: 20019 Balance: $100.00")


if __name__ == "__main__":
    unittest.main()
