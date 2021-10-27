# Creating a Budget class to calculate budgets and expenses

class Expenditure:
    def __init__(self, income, budget, tax):
        self.income = income
        self.budget = budget
        self.tax = tax

    def tax_amount(self):
        return self.income*(self.tax/100)

    def expenses(self):
        return self.income(1 - (self.tax/100)) - self.budget
