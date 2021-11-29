# Money_Advisor

This is a full fledged application coded in Python to track your expenses, budget and savings. This program asks users to input data related to finances like budget, expenditure, savngs, basics, tax etc.

## Motivation
* This is the first time I am actually going to commit to a project for something useful, unlike the previous projects that were only coded for learning purposes.
* The ideas and features that come to my mind related to this project motivates me to start this project.

## Concepts used
* Python Basics
* Classes and Objects
* Static Methods
* Math module
* Conditionals
* Functions

## Components of the Money App
There are two main components to this app:

* Expenditure --Allocator-- Calculator
  * The purpose of this component is to give you an idea on how much you should spend on your expenses (Eg: Food, Education, Recreation, Other Basics etc), given the budget and the tax.
  * For example, suppose you want to buy a pricey laptop. Obviously, you want to cut on expenses in order to buy it. So, given your monthly income, the price of the laptop (aka budget) and taxes (in percentage), this component will tell you how much you have to spend on your expenses per month.
  * This component supposes that your budget is fulfilled in one month only.

* <u>Budget Calculator</u>
  * The purpose of this component is to calculate the monthly budget from the monthly income and monthly expenses.
  * It allows you to calculate the budget divided between the number of months given by the user.
  * It also allows you to calculate the number of months it takes to satisfy the total budget if the monthly budget is not enough.

## Methods in class "Expenditure"
* <u>__init__(self, income, budget, tax)</u>: Takes monthly income, monthly budget, tax(in %) as parameters
* <u>tax()</u>: Returns the amount of income to be paid as tax
* <u>expenses()</u>: Returns the remaining income after monthly budget and tax are deducted
* <u>allocate()</u>: This is the most important method in this component. It takes the remaining income and splits it among food, basicities, education, recreation and savings. The percentage of division is based on the optimal planning.
* <u>budget()</u>: Returns budget amount after subtracting monthly expenses from the monthly income
* <u>months_needed(self, total_budget)</u>: Returns the number of months needed to fulfil the total budget parameter after dividing it by the monthly budget. It uses math module to round up the number of months to a whole number.
* <u>budget_per_month(total_budget, time)</u>: It is a static method which takes time (in months as integer) and total budget as parameters and divides the total budget by the given number of months to satisfy the budget per month.

*More information will be added later*





### Created by
*Khair Al Anam*
