#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 21:36:47 2017

@author: pablo
"""

# Generating white noise
import numpy as np
import matplotlib.pyplot as plt
x = np.random.randn(100)
plt.plot(x)
plt.show()


# for loop
import numpy as np
import matplotlib.pyplot as plt
ts_length = 100
epsilon_values = []
# Empty list
for i in range(ts_length):
    e = np.random.randn()
    epsilon_values.append(e)
plt.plot(epsilon_values, 'b-')
plt.show()

# while
import numpy as np
import matplotlib.pyplot as plt
ts_length = 100
epsilon_values = []
i = 0
while i < ts_length:
    e = np.random.randn()
    epsilon_values.append(e)
    i = i + 1
plt.plot(epsilon_values, 'b-')
plt.show()

# UDF
import numpy as np
import matplotlib.pyplot as plt
def generate_data(n):
    epsilon_values = []
    for i in range(n):
        e = np.random.randn()
        epsilon_values.append(e)
    return epsilon_values

data = generate_data(100)
plt.plot(data, 'b-')
plt.show()

# Random uniform vs random normal
import numpy as np
import matplotlib.pyplot as plt
def generate_data(n, generator_type):
    epsilon_values = []
    for i in range(n):
        if generator_type == 'U':
            e = np.random.uniform(0, 1)
        else:
            e = np.random.randn()
        epsilon_values.append(e)
    return epsilon_values

data = generate_data(100, 'U')
plt.plot(data, 'b-')
plt.show()


# Pass the desired generator type as a function

import numpy as np
import matplotlib.pyplot as plt
def generate_data(n, generator_type):
    epsilon_values = []
    for i in range(n):
        e = generator_type()
        epsilon_values.append(e)
    return epsilon_values
data = generate_data(100, np.random.uniform)
plt.plot(data, 'b-')
plt.show()

#
import numpy as np
import matplotlib.pyplot as plt
def generate_data(n, generator_type):
    epsilon_values = [generator_type() for _ in range(n)]
    return epsilon_values
data = generate_data(100, np.random.uniform)
plt.plot(data, 'b-')
plt.show()


# Nerd joke
import antigravity

def main():
    antigravity.fly()

if __name__ == '__main__':
    main()
    