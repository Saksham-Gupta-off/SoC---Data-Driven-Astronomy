#!/usr/bin/env python
# coding: utf-8

# In[31]:


import random
import matplotlib.pyplot as mat

list_sum = []
largenumber = 36**3 # It is a large number, could be anything

for i in range(0, largenumber): 
    list_sum.append(random.randint(1,6) + random.randint(1,6))


# In[40]:


mat.hist(list_sum, bins=11, density=True)
mat.xlabel("Sum")
mat.ylabel("Probability")
mat.title("Probability of sum of values on rolling a pair of die")
mat.show()

