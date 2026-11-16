"""Tests for the AccountStatus enumeration."""

import unittest

from account.account_status import AccountStatus


class TestAccountStatus(unittest.TestCase):
    def test_enumeration_values_are_initialized(self):
        self.assertEqual(AccountStatus.ACTIVE.value, 1)
        self.assertEqual(AccountStatus.CLOSED.value, 2)
        self.assertEqual(AccountStatus.FROZEN.value, 3)
        self.assertEqual(len(AccountStatus), 3)


if __name__ == "__main__":
    unittest.main()
