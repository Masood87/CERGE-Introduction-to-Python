#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 22:28:08 2017

@author: pablo
"""
#######################
## Primitive data types
#######################

# Boolean

x = True
y = 100 < 10
y
type(y)

x*y
x+y

bools = [True, False, True, False]
sum(bools)

# Integers and floats

a, b = 1, 2
a+b
type(a)

c, d = 2.5, 10.0
type(c)

# Python 3.5+
a/b

# Complex numbers
x = complex(2,1)
y = complex(1,2)

x*y 


# String
x = "I am a string "
y = "... am I not?"
x+y
type(x)

'Hi '*4


#######################
## Containers
#######################
# Lists
x = [1,'a',2.0]
type(x)

x[0]
x[0] = 3
x



# Tuples
y = (1,'a',1.0)
y[0]
y[0] = 3
type(y)

# Tuples and lists can be unpacked

names = ('Juan', 'Pablo', 'Maldonado')
first, second, first_last_name = names
print(first)



# String to list
single_line = 'pablo,maldonado,zizkov'
my_data = single_line.split(',')
name, last_name, address = 'pablo,maldonado,zizkov'.split(',')


# and back
new_single_line = ','.join(my_data)
new_single_line
new_single_line == single_line




#Slice notation: a[m:n] returns n-m elements starting on m
a = [2,4,6,8]
a[2:3]
a[-1]
a[-2:]


s = 'cergeiscool'
s[:5]

#Dictionaries: key-value pairs
d = {'name':'Pablo', 'last_name':'Maldonado'}
d['name']
d['address']

# Sets 
s = [1,2,3,1,2,1,1,2]
set(s)


s1 = {'a','b'}
s2 = {'b','c'}
s1.issubset(s2)
s1.intersection(s2)

#######################
## Importing
#######################

import math
math.sqrt(4)

from math import * 
sqrt(4)

from math import sqrt
sqrt(4)


#######################
## Input and output
#######################

#where are we?
import os

print(os.getcwd())


f = open('newfile.txt', 'w')
f.write('Test \n')
f.write('Another test')
f.close()

f = open('newfile.txt','r')
out = f.read()
out
print(out)


my_data = open('cz_cities.txt','r')
print(my_data.read()) # reads it all and closes the file

my_data = open('cz_cities.txt','r')
for line in my_data:
    city, value = line.split(':') # Unpack
    city = city.title() # Capitalize
    value = '{0:,}'.format(int(value)) #Add commas
    print(city.ljust(15)+value)
my_data.close()    


#######################
## Looping 
#######################

x_vals = [1,2,3,4,5]
for x in x_vals:
    print(x*x)

for i in range(len(x_vals)):
    print(x_vals[i]*x_vals[i])
    
    
# Loop through pairs of sequences
countries = ('Czechia','Mexico','Germany')
cities = ('Prague','Morelia','Munich')

for country, city in zip(countries, cities):
    print('{1} is a city in {0}'.format(country,city))    


dict(zip(countries, cities))    

# If we actually need the index, we can use enumerate
for index, city in enumerate(cities):
    print("{1} has index {0}".format(index,city))
    

# Accumulate
countries = ('Czechia','Mexico','Germany', 'Mexico','Czechia','Mexico')

# how many times is Mexico there?

n_times = 0
for country in countries:
    if country == 'Mexico':
        n_times +=1
        
print('Mexico was on the list {0} times'.format(n_times))        

# Looping over a dictionary

days = {'mon':'Monday', 'tue':'Tuesday', 'wed':'Wednesday',\
        'thu':'Thursday','fri':'Friday'}

for day in days:
    print('{0} stands for {1}'.format(day,days[day])) 


# Fibonacci numbers
a = 0
b = 1
n = 10
while a<=n:
    c = a+b
    a = b
    b = c
    print(c)
#######################
## Comparisons  
#######################
x,y = 1,2
x<y
x>y    
    
1<2<3
1<=2<=3    
1<2>3
    
    
x = 1 # Assignment
x == 2 #Comparison    
    
1 != 2

# online if-else 
# val_true if condition else val_false

x = 'yes' if 2>3 else 'no'    
x
    
x = 'yes' if 2<3 else 'no'    
x
    
    
x = 'yes' if 1<2 and 'f' in 'foo' else 'no'        
x

#######################
## Functions in Python 
#######################

max(19,20)
min(19,20)
sum([19,20])
str(22)
type(22)  
len([19,20,21])
18 % 2
19 % 2
    
def pos_or_neg(x):
    if x<0:
        return 'negative'
    return 'non-negative'

pos_or_neg(-3)
pos_or_neg(5)

#Functions without return statement will return a special Python object, None

def square(x):
    """
    This function returns the square of a number
    """ 
    return x**2

#square?
#square??
square(2)

## On-line functions / anonymous functions
square = lambda x: x**2
square(2)

from scipy.integrate import quad
quad(lambda x: x**2, 0,1)

my_vals = [0,1,2,3]
my_vals_squared = [x**2 for x in my_vals]    
my_vals_squared 

my_vals = range(10) #0 to n-1
my_vals_squared = [x**2 for x in my_vals]    
my_vals_squared 


my_vals = range(1,11) #including the first, excluding the last
my_vals_squared = [x**2 for x in my_vals]    
my_vals_squared

#################################
#################################
##
##      Exercises
## 
#################################
#################################

# 1a. Compute the inner product of two vectors, x,y of the same size
# 1b. Count the number of even numbers in 0:99
#       # Hint: x%2 returns 0 if x is even, 1 otherwise
# 1c: Given a list of tuples 
# [(2,5),(4,2),(9,8), (12,11)] count the number of pairs 
#        such that both a and b are even

# 2. Count the number of capital letters in a string. 
#   Hint: 'hi'.upper() returns 'HI'

#3. Write a function poly(x,coeff)

#4. Write a function that, for given n, draws
#this triangle

#*
#* *
#* * *

# Factorial(n)