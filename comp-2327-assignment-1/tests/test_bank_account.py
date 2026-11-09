import unittest

from account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    """Test cases for BankAccount."""

    def setUp(self):
        """Set up a bank account for testing."""
        self.account = BankAccount(client_id=1, initial_balance=1000.0)

    def test_initialization(self):
        """Verify the bank account is initialized correctly."""
        self.assertEqual(self.account.client_id, 1)
        self.assertEqual(self.account.balance, 1000.0)

    def test_deposit(self):
        """Test deposit functionality."""
        self.account.deposit(500.0)
        self.assertEqual(self.account.balance, 1500.0)

    def test_withdraw(self):
        """Test withdraw functionality."""
        self.account.withdraw(200.0)
        self.assertEqual(self.account.balance, 800.0)

    def test_withdraw_insufficient_funds(self):
        """Test withdrawing more than the balance raises an error."""
        with self.assertRaises(ValueError):
            self.account.withdraw(1500.0)

if __name__ == "__main__":
    unittest.main()
