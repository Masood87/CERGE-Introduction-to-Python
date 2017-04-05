#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 17:37:31 2017

@author: pablo
"""

################################
#################################
##
##      Exercises
## 
#################################
#################################

# 1a. Compute the inner product of two vectors, x,y of the same size


# 1.a
x = [1,2,3]
y = [4,5,6]

def inner(x,y):
    acc = 0
    for i in range(len(x)):
        acc += x[i]*y[i]
    return acc

inner(x,y)     


# Factorial(n)
def factorial(n):
    acc = 1
    for i in range(1,n+1):
        acc *= i
    return acc

factorial(4)

#3. Write a function poly(x,coeff)

def poly(x,coeffs):
    val = 0
    for i, coeff in enumerate(coeffs):
        val += coeff*x**i
    return val

poly(1,[1,2,1])


# 4. 
import matplotlib.pyplot as plt
import numpy as np
def corr_ts(alpha, T):
    xt=0
    t=0
    vals = []
    while t<T:
        vals.append(xt)
        xt = alpha*xt+np.random.randn()
        t+=1
    return vals

plt.plot(corr_ts(0.9,200))
plt.show()

# 5
def estimate_pi(N=1000):
    n = 0
    area = 0.0
    while n<N:
        x = np.random.uniform(0,1)
        y = np.random.uniform(0,1)
        area += 1/N if (x-1/2)**2+(y-1/2)**2<=1/4 else 0
        n+=1
    return 4*area

estimate_pi(100000)        