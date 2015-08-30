# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 11:09:11 2015

@author: Doug
"""
'''
Python Homework with Chipotle data
https://github.com/TheUpshot/chipotle
'''

'''
BASIC LEVEL
PART 1: Read in the file with csv.reader() and store it in an object called 'file_nested_list'.
Hint: This is a TSV file, and csv.reader() needs to be told how to handle it.
      https://docs.python.org/2/library/csv.html
'''

with open('chipotle.tsv', mode = 'rU') as f:
    file_nested_list = [row for row in csv.reader(f, delimiter = '\t')]

'''
BASIC LEVEL
PART 2: Separate 'file_nested_list' into the 'header' and the 'data'.
'''

header = file_nested_list[0]
data = file_nested_list[1:]

data[0:10]

'''
INTERMEDIATE LEVEL
PART 3: Calculate the average price of an order.
Hint: Examine the data to see if the 'quantity' column is relevant to this calculation.
Hint: Think carefully about the simplest way to do this!
'''

average_order_price =  (sum([float(row[4][1:]) for row in data]))/1834

'''
INTERMEDIATE LEVEL
PART 4: Create a list (or set) of all unique sodas and soft drinks that they sell.
Note: Just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'.
'''

cokes = []

for row in data:
    if row[2] == 'Canned Soda' or row[2] == 'Canned Soft Drink':   
        cokes.append(row[3])
print set(cokes)

'''
ADVANCED LEVEL
PART 5: Calculate the average number of toppings per burrito.
Note: Let's ignore the 'quantity' column to simplify this task.
Hint: Think carefully about the easiest way to count the number of toppings!
'''
burritos = []

for row in data:
    if row[2][-7:] == 'Burrito':
        burritos.append(float(row[3].count(','))+1)
        
print (sum((burritos))/ len(burritos))

'''
ADVANCED LEVEL
PART 6: Create a dictionary in which the keys represent chip orders and
  the values represent the total number of orders.
Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
Note: Please take the 'quantity' column into account!
Optional: Learn how to use 'defaultdict' to simplify your code.
'''
from collections import defaultdict

chips = []

d = defaultdict(int)
for chip in data:
    if 'Chips' in chip[2]:
        d[chip[2]] += int(chip[1])
dict(d)


'''
BONUS: Think of a question about this data that interests you, and then answer it!
'''

#Im only interested in eating Chipotle now


