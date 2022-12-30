<!DOCTYPE html>
<html>
<head>
</head>
<body>
	<h1>Welcome to Python Pizza Deliveries!</h1>
	<p>This module allows you to calculate the price of a pizza, regardless of size and add-ons, with just a few lines of code.</p>
	<p>Pricing:</p>
	<ul>
		<li>Small pizza: $15</li>
		<li>Medium pizza: $20</li>
		<li>Large pizza or other sizes: $25</li>
	</ul>
	<p>Add-ons:</p>
	<ul>
		<li>Extra pepperoni (all sizes): $1</li>
		<li>Extra cheese (all sizes): $1</li>
	</ul>
	<p>To use this module, simply input the size of the pizza you want (S, M, or L), and whether or not you want pepperoni or extra cheese (Y or N). The module will then calculate the total price for you.</p>
	<pre>
		<code>
			# Variables to store user's input
			size = input("What size pizza do you want? S, M, or L ")
			add_pepperoni = input("Do you want pepperoni? Y or N ")
			extra_cheese = input("Do you want extra cheese? Y or N ")
Copy code
		# A variable with 0 which we will use for addition
		bill = 0
		if size == 'S':
		    bill +=15
		elif size == 'M':
		    bill +=20
		else:
		    bill +=25
		    
		# Consitional statements to consider add-ons
		if add_pepperoni == 'Y':
		    if size == 'S':
		        bill +=2
		    else:
		        bill +=3
		        
		if extra_cheese == 'Y':
		    bill +=1
		    
		print(f'your total pizza price is {bill}')
	</code>
</pre>
</body>
</html>
