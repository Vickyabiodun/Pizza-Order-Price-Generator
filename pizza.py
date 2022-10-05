"""This module allows you calculate pizza prize irrespective of size and add-ons with few lines of code"""

print("Welcome to Python Pizza Deliveries!")
"""
small pizza is 15, medium is 20 and large or others is 25
extra pepperoni on small is 2 while other sizes is 3
extra chesse on all sizes is 1

"""

"""Variables to store user's input"""
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

"""A variable with 0 which we will use for addition"""
bill = 0
if size == 'S':
    bill +=15
elif size == 'M':
    bill +=20
else:
    bill +=25
    
"""Consitional statements to consider add-ons"""
if add_pepperoni == 'Y':
    if size == 'S':
        bill +=2
    else:
        bill +=3
        
if extra_cheese == 'Y':
    bill +=1
    
print(f'your total pizza price is {bill}')