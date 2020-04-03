###    Author Suresh Chinta
###    Date April 1st 2020
###    is_convex_function return True if a function is convex between two x values x1 and x2
###    works for single variable functions/one dimensional function

import numpy as np
import random
import math

def power2_func(x):
    return(x**2)

def sin_func(x):
    return(math.sin(x))

def cos_func(x):
    return(math.cos(x))

def func_abs(x):
    return(np.absolute(x))

def is_convex_function(func, x1, x2, is_strictly = False):
    """
    func : any function that takes one argument and returns f(x)
    x1 : value of x coordinate
    x2 : value of x coordinate > x1
    is_strictly : check for strict convexity	
    """
    for i in range(0,100):
        theta = random.uniform(0,1)
        x3 = theta * x1 + (1 - theta) * x2
        #print(round(x3,2), round(theta,2), func(x1), func(x2), func(x3))       

        if (is_strictly):
            check_for_convexity = (theta * func(x1) + (1 - theta) * func(x2)) > func(x3)
        else:
            check_for_convexity = (theta * func(x1) + (1 - theta) * func(x2)) >= func(x3)
            
        if (check_for_convexity):            
            pass
        else:
            #print(f'function is not convex at x {round(x3,2)}, theta :  {round(theta,2)}, between {x1} and {x2} function value : {round(func(x3),2)}, value on line : {round(theta * func(x1) + (1 - theta) * func(x2), 2)}')
            return(False)
    #print(f'function is convex between {x1} and {x2}')
    return(True)


# testing
help(is_convex_function)
print(is_convex_function(power2_func, 2, 5))
print(is_convex_function(math.sin, 2, 5))
print(is_convex_function(math.cos, 2, 5))
print(is_convex_function(np.abs, 3, 5, True))
