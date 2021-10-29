# Creating class Expenditure to calculate expenses and allocate them to its subsets

class Expenditure:

    # Takes monthly income, budget, tax(in %) as parameters
    def __init__(self, income, budget, tax):
        self.income = income
        self.budget = budget
        self.tax = tax

    # Returns the amount of income to be paid as tax
    def tax_amount(self):
        return self.income*(self.tax/100)

    # Returns the remaining income after tax and budget are deducted from the total income
    def expenses(self):
        return self.income*(1 - (self.tax/100)) - self.budget

    # Allocates the remaining income to the subsets like food, basicities etc
    def allocate(self):
        Expenses = self.income*(1 - (self.tax/100)) - self.budget
        food = 0.25 * Expenses
        education = 0.3 * Expenses
        basicities = 0.15 * Expenses
        recreation = 0.1 * Expenses
        total_spent = food + basicities + recreation + education
        savings = Expenses - total_spent
        return f"Your optimal expenditure is as follows: \
            Food expenses: {food} \
            Education: {education} \
            Basicities: {basicities} \
            Recreation/Entertainment: {recreation} \
            Savings: {savings} \
            Total spent: {total_spent}"


E1 = Expenditure(6000, 1000, 5)
print(E1.allocate())
