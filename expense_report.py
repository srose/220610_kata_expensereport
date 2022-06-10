import locale
from datetime import datetime
from enum import Enum, unique, auto
from typing import List


@unique
class ExpenseType(Enum):
    DINNER = auto()
    BREAKFAST = auto()
    LUNCH = auto()
    CAR_RENTAL = auto()


class Expense:
    type: ExpenseType
    amount: int


def is_meal(expense_type):
    return expense_type == ExpenseType.DINNER \
           or expense_type == ExpenseType.BREAKFAST \
           or expense_type == ExpenseType.LUNCH


class ExpenseReport:
    def get_expense_type_name(self, expense_type):
        if expense_type == ExpenseType.DINNER:
            return "Dinner"
        
        if expense_type == ExpenseType.BREAKFAST:
            return"Breakfast"
        
        if expense_type == ExpenseType.CAR_RENTAL:
            return "Car Rental"
        
        if expense_type == ExpenseType.LUNCH:
            return "Lunch"
        
        return ""

    def print_report(self, expenses: List[Expense]):
        total = 0
        meals = 0

        #print("Expense Report", datetime.now().strftime(locale.nl_langinfo(locale.D_T_FMT)))

        for expense in expenses:
            expense_type = expense.type
            if is_meal(expense_type):
                meals += expense.amount

            name = self.get_expense_type_name(expense_type)

            meal_over_expenses_marker = "X" if expense_type == ExpenseType.DINNER and expense.amount > 5000 or expense_type == ExpenseType.BREAKFAST and expense.amount > 1000 else " "
            print(name, "\t", expense.amount, "\t", meal_over_expenses_marker)
            total += expense.amount

        print("Meals:", meals)
        print("Total:", total)
