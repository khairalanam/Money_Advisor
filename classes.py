# Creating class Expenditure to calculate expenses and allocate them to its subsets

class Expenditure:

    def __init__(self, income, budget, tax):
        self.income = income
        self.budget = budget
        self.tax = tax

    def tax_amount(self):
        return self.income*(self.tax/100)

    def expenses(self):
        return self.income*(1 - (self.tax/100)) - self.budget

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

# Creating class Budget to calculate monthly budget from income, expenses and total budget for an item


class Budget:

    def __init__(self, income, expenses, total_budget):
        self.income = income
        self.expenses = expenses
        self.total_budget = total_budget

    def budget(self):
        return self.income - self.expenses

    def months_needed(self):
        from math import ceil

        time_needed = self.total_budget / self.budget
        if self.total_budget % self.budget == 0:
            return time_needed
        else:
            if ceil(time_needed) - time_needed == 0.5:
                return time_needed
            else:
                return ceil(time_needed)

    def budget_per_month(self, time):
        from math import ceil

        return ceil(self.total_budget / time)
