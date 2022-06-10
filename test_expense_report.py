import unittest

from expense_report import Expense, ExpenseType, is_meal


class ExpenseReportTest(unittest.TestCase):
    def test_is_meal(self):
        self.assertEqual(True, is_meal(ExpenseType.LUNCH))
        self.assertEqual(True, is_meal(ExpenseType.BREAKFAST))
        self.assertEqual(True, is_meal(ExpenseType.DINNER))

    def test_is_not_meal(self):
        self.assertEqual(False, is_meal(ExpenseType.CAR_RENTAL))



if __name__ == '__main__':
    unittest.main()
