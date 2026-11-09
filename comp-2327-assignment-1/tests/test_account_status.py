import unittest

from account.account_status import AccountStatus


class TestAccountStatus(unittest.TestCase):
    """Tests for the account status enumeration values."""

    def test_enum_values_are_initialized(self):
        """Each defined status has the integer value from the class design."""
        self.assertEqual(AccountStatus.INACTIVE.value, 0)
        self.assertEqual(AccountStatus.ACTIVE.value, 1)
        self.assertEqual(AccountStatus.SUSPENDED.value, 2)
        self.assertEqual(AccountStatus.CLOSED.value, 3)


if __name__ == "__main__":
    unittest.main()
