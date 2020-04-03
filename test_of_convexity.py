#!/usr/bin/env python
# coding: utf-8

# In[89]:


###    Author Suresh Chinta
###    Date April 1st 2020
###    is_convex_function return True if a function is convex between two x values x1 and x2
###    works for single variable functions/one dimensional function


# In[90]:


import numpy as np
import random
import math


# In[91]:


def power2_func(x):
    return(x**2)


# In[92]:


def sin_func(x):
    return(math.sin(x))


# In[93]:


def cos_func(x):
    return(math.cos(x))


# In[121]:


def is_convex_function(func, x1, x2):
    """
    func : any function that takes one argument and returns f(x)
    x1 : value of x coordinate
    x2 : value of x coordinate > x1
    """
    for i in range(0,100):
        theta = random.uniform(0,1)
        x3 = theta * x1 + (1 - theta) * x2
        check_for_convexity = theta * func(x1) + (1 - theta) * func(x2) >= func(x3)
        if (check_for_convexity is True):            
            pass
        else:
            print(f'function is not convex at : {round(x3,2)}, beteen {x1} and {x2} function value : {round(func(x3),2)}, value on line : {round(theta * func(x1) + (1 - theta), 2)}')
            return(False)
    print(f'function is convex between {x1} and {x2}')
    return(True)


# In[122]:


help(is_convex_function)


# In[123]:


print(is_convex_function(power2_func, 2, 5))


# In[124]:


is_convex_function(math.sin, 2, 5)


# In[125]:


is_convex_function(math.cos, 2, 5)

