<h1>Python Pizza Deliveries</h1>

<p>This module allows you to calculate the price of a pizza with a few lines of code, regardless of the size or any add-ons.</p>

<h2>Getting Started</h2>

<p>To use this module, you will need to have Python 3 installed on your computer.</p>

<h3>Prerequisites</h3>

<p>Make sure you have Python 3 installed on your system. You can check by running the following command in your terminal:</p>

<pre>
python --version
</pre>

<p>If you don't have Python 3 installed, you can download it from the <a href="https://www.python.org/downloads/">official website</a>.</p>

<h3>Installing</h3>

<p>No installation is required to use this module. Simply copy and paste the code into a Python file and run it.</p>

<h2>Usage</h2>

<p>To use the module, run the following code:</p>

<pre>
print("Welcome to Python Pizza Deliveries!")
</pre>

<p>The module will prompt you to enter the size of the pizza you want (S, M, or L), whether you want pepperoni (Y or N), and whether you want extra cheese (Y or N).</p>

<pre>
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
</pre>

<p>The module will then calculate the price of the pizza based on the size and any add-ons.</p>

<pre>
bill = 0
if size == 'S':
    bill +=15
elif size == 'M':
    bill +=20
else:
    bill +=25

if add_pepperoni == 'Y':
    if size == 'S':
        bill +=2
    else:
        bill +=3

if extra_cheese == 'Y':
    bill +=1

print(f'your total pizza price is {bill}')
</pre>

<h2>Examples</h2>

<p>Here are some examples of how to use the module:</p>

<pre>
>>> size = 'M'
>>> add_pepperoni = 'Y'
>>> extra_cheese = 'N'
>>> your total pizza price is 23
</pre>

<pre>
>>> size = 'L'
>>> add_pepperoni = 'N'
>>> extra_cheese = 'Y'
>>> your total pizza price is 26
</pre>

<h2>Notes</h2>

<ul>
  <li>The base price for a small pizza is 15, a medium pizza is 20, and a large or other size pizza is 25.</li>
  <li>The additional cost for extra pepperoni on a small pizza is 2, and, and the cost for all other sizes is 3.</li>
  <li>The additional cost for extra cheese on any size pizza is 1.</li>
<h2>Authors</h2>
<ul>
  <li>[Abiodun Victoria] - https://github.com/Vickyabiodun</li>
</ul>
<h2>License</h2>
<p>This project is licensed under the MIT License - see the <a href="LICENSE.md">LICENSE.md</a> file for details.</p>
