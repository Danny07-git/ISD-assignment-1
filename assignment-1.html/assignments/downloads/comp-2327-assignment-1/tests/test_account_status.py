
"""
Unit tests for the AccountStatus enumeration.
"""

import unittest

from account.account_status import AccountStatus


class TestAccountStatus(unittest.TestCase):
    """Test cases for AccountStatus."""

    def test_enumeration_values(self):
        """Verify all enumeration values are initialized."""

        self.assertEqual(AccountStatus.INACTIVE.value, 0)
        self.assertEqual(AccountStatus.ACTIVE.value, 1)
        self.assertEqual(AccountStatus.SUSPENDED.value, 2)
        self.assertEqual(AccountStatus.CLOSED.value, 3)


if __name__ == "__main__":
    unittest.main()
