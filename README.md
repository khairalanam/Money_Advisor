# Money_App

This is a full fledged application coded in Python to track your expenses, budget and savings. This program asks users to input data related to finances like budget, expenditure, savngs, basics, tax etc.

## Motivation
* This is the first time I am actually going to commit to a project for something useful, unlike the previous projects that were only coded for learning purposes.
* The ideas and features that come to my mind related to this project motivates me to start this project.

## Concepts used
* Python Basics
* Classes and Objects
* Static Methods

## Components of the Money App
There are three main components to this app (Many will be added later):

* Expenditure Allocator
  * The purpose of this component is to give you an idea on how much you should spend on your expenses (Eg: Food, Education, Recreation, Other Basics etc), given the budget and the tax.
  * For example, suppose you want to buy a pricey laptop. Obviously, you want to cut on expenses in order to buy it. So, given your monthly income, the price of the laptop (aka budget) and taxes (in percentage), this component will tell you how much you have to spend on your expenses per month.
  * This component supposes that your budget is fulfilled in one month only.


## Methods in each component
* Expenditure allocator:
 * __init__(): Takes monthly income, budget, tax(in %) as parameters
 * tax(): Returns the amount of income to be paid as tax
 * expenses(): Returns the remaining income after budget and tax are deducted
 * allocate(): This is the most important method in this component. It takes the remaining income and splits it among food, basicities, education, recreation and savings. The percentage of division is based on the optimal planning.



*More information will be added later*





### Created by
*Khair Al Anam*
