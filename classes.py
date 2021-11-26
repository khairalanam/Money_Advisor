# Creating class Expenditure to calculate expenses and allocate them to its subsets

class Expenditure:

    def __init__(self, income, monthly_budget, tax):
        self.income = income
        self.monthly_budget = monthly_budget
        self.tax = tax

    def tax_amount(self):
        return self.income*(self.tax/100)

    def expenses(self):
        return self.income*(1 - (self.tax/100)) - self.monthly_budget

    def budget(self):
        spendings = Expenditure.expenses(self)
        return self.income - spendings

    def allocate(self):
        Expenses = self.income*(1 - (self.tax/100)) - self.monthly_budget
        food = 0.25 * Expenses
        education = 0.3 * Expenses
        basicities = 0.15 * Expenses
        recreation = 0.1 * Expenses
        Tax = self.income*(self.tax/100)
        total_spent = food + basicities + recreation + education + Tax
        savings = Expenses - total_spent
        return f"""Your optimal expenditure is as follows:
            Food expenses: {food}
            Education: {education}
            Basicities: {basicities}
            Recreation/Entertainment: {recreation}
            Tax = {Tax}
            Savings: {savings}
            Total spent: {total_spent}"""

    def months_needed(self, total_budget):
        from math import ceil

        time_needed = total_budget / self.monthly_budget
        if total_budget % self.monthly_budget == 0:
            return time_needed
        else:
            if ceil(time_needed) - time_needed == 0.5:
                return time_needed
            else:
                return ceil(time_needed)

    @staticmethod
    def budget_per_month(total_budget, time):
        from math import ceil

        return ceil(total_budget / time)
