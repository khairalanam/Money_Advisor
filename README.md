# Money_Advisor

This is a full fledged program coded in Python to track your expenses, budget and savings. This program asks users to input data related to finances like budget, expenditure, savngs, basics, tax etc.

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
* Object-Oriented Programming
* Functional Programming

## Components of the Money App
There are two main components to this app:

* Expenditure ~~Allocator~~ Calculator
  * The purpose of this component is to give you an idea on how much you should spend on your expenses (Eg: Food, Education, Recreation, Other Basics etc), given the budget and the tax.
  * For example, suppose you want to buy a pricey laptop. Obviously, you want to cut on expenses in order to buy it. So, given your monthly income, the price of the laptop (aka budget) and taxes (in percentage), this component will tell you how much you have to spend on your expenses per month.
  * This component supposes that your budget is fulfilled in one month only.

* <u>Budget Calculator</u>
  * The purpose of this component is to calculate the monthly budget from the monthly income and monthly expenses.
  * It allows you to calculate the budget divided between the number of months given by the user.
  * It also allows you to calculate the number of months it takes to satisfy the total budget if the monthly budget is not enough.

## Sub-components of each Component
There are three sub-components to each of the two components of the program:

* Expenditure Calculator:
  1. Monthly Expenditure Calculator
    * Calculates your monthly expenses given the monthly income, tax rate and monthly budget.
  2. Tax Calculator
    * Calculates your monthly tax to be paid given the monthly income, tax rate and monthly budget.
  3. Expenditure Allocator
    * Gives the optimal expenditure plan based on the monthly income, tax rate and the monthly budget.
    
* Budget Calculator
  1. Monthly Budget Calculator
    * Calculates the ***actual*** monthly budget based on the optimal expenditure plan which is derived from the monthly income, monthly budget (input by user) and the tax rate. This one includes the user-input budget PLUS the savings which is derived from the optimal expenditure plan.
  2. Time Calculator
    * Calculates the number of months required to fulfill the total budget (not monthly) input by user based on the given monthly budget, monthly income and tax rate.
  3. Budget per Month Calculator
    * Calculates the monthly budget to be maintained in order to fulfill a total budget in theset number of months, both input by the user.

## Methods in class "Expenditure"
* <u>__init__(self, income, budget, tax)</u>: Takes monthly income, monthly budget, tax(in %) as parameters
* <u>tax()</u>: Returns the amount of income to be paid as tax
* <u>expenses()</u>: Returns the remaining income after monthly budget and tax are deducted
* <u>allocate()</u>: This is the most important method in this component. It takes the remaining income and splits it among food, basicities, education, recreation and savings. The percentage of division is based on the optimal planning.
* <u>budget()</u>: Returns budget amount after subtracting monthly expenses from the monthly income
* <u>months_needed(self, total_budget)</u>: Returns the number of months needed to fulfil the total budget parameter after dividing it by the monthly budget. It uses math module to round up the number of months to a whole number.
* <u>budget_per_month(total_budget, time)</u>: It is a static method which takes time (in months as integer) and total budget as parameters and divides the total budget by the given number of months to satisfy the budget per month.

*Thanks for reading! :D*

### Created by
*Khair Al Anam*
