# Python Pizza Deliveries
This module allows you to calculate the price of a pizza with a few lines of code, regardless of size and add-ons.

# Usage
First, import the module:

import pizza_deliveries
Then, use the following code to calculate the price of your pizza:

Copy code
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
else:
    bill += 25
    
if add_pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3
        
if extra_cheese == 'Y':
    bill += 1
    
print(f'Your total pizza price is {bill}')

# Prices

Small pizzas are 15.
Medium pizzas are 20.
Large pizzas or others are 25.
Extra pepperoni on small pizzas is 2, on other sizes is 3.
Extra cheese on all sizes is 1.
