from classes import Expenditure

# Functions used


def y_or_n():
    global yes_or_no
    yes_or_no = input("Continue? (y/n): ")
    if yes_or_no in ["y", "n"]:
        return yes_or_no
    else:
        print("Invalid input!")
        y_or_n()


# Main Program
print("Welcome to the Money Advisor!")
print("1. Expenditure Allocator")
print("2. Budget Calculator")
print("3. (Coming Soon)")

selector = int(input(
    "Type the number to proceed to any one of the three components mentioned above: "))

yes_or_no = "y"

# Expenditure Allocator Component

if selector == 1:
    while yes_or_no != "n":
        income = int(input("Enter your monthly income(in dollars): "))
        budget = int(input("Enter your monthly budget(in dollars): "))
        tax = int(input("Enter the monthly tax rate(in %): "))
        expense = Expenditure(income, budget, tax)
        print(expense.allocate())
        print("*****************************")
        yes_or_no = y_or_n()

# Budget Calculator Component

if selector == 2:
    while yes_or_no != "n":
        income = int(input("Enter your monthly income(in dollars): "))
        budget = int(input("Enter your monthly budget(in dollars): "))
        tax = int(input("Enter the monthly tax rate(in %): "))
        expense = Expenditure(income, budget, tax)

        print("1. Monthly Budget Calculator")
        print("2. Time Calculator")
        print("3. Budget per Month Calculator")
        budget_selector = int(input(
            "Enter the number to proceed to any one of the above mentioned sub-components: "))

        if budget_selector == 1:
            print(
                f"Your monthly budget is {expense.budget()} dollars per month")

        if budget_selector == 2:
            total = int(input("Type in the total budget to be fulfilled: "))
            print(
                f"You will need {expense.months_needed(total)} months to  fulfill your full budget, given that your monthly budget is {expense.budget()} dollars.")

        if budget_selector == 3:
            full_budget = int(
                input("Type in the total budget to be fulfilled: "))
            time = int(
                input("Type in the number of months required to fulfill the total budget: "))
            print(
                f"You will need to have a monthly budget of f{Expenditure.budget_per_month(full_budget, time)} dollars per month in order to fulfill your total budget of {full_budget} within {time} months.")

        yes_or_no = y_or_n()

#
