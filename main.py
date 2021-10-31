from classes import Expenditure
# Main Program

# Expenditure Allocator Component
yes_or_no = "y"

while yes_or_no != "n":
    income = int(input("Enter your monthly income(in dollars): "))
    budget = int(input("Enter your total budget(in dollars): "))
    tax = int(input("Enter the monthly tax rate(in %): "))
    expense = Expenditure(income, budget, tax)
    print(expense.allocate())
    print("*****************************")
    yes_or_no = input("Continue? (y/n): ")
    if yes_or_no in ["y", "n"]:
        pass
    else:
        print("Invalid input!")
        continue
