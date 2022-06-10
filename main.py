from expense_report import ExpenseReport, Expense, ExpenseType

# Coders of the day:
# Sebastian Rose
# Anna Maier
# Richard von Faber
# Chris Coltsman

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    expense = Expense()
    expense.type = ExpenseType.LUNCH
    expense.amount = 7500
    ExpenseReport().print_report([expense])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
