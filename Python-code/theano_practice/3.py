# coding:utf-8

"""
Author: roguesir
Date: 2017/8/30
GitHub: https://roguesir.github.com
Blog: http://blog.csdn.net/roguesir
"""

import numpy as np
import theano
import theano.tensor as T


state = theano.shared(np.array(0,dtype=np.float64))
inc = T.scalar('inc',dtype=state.dtype)
accumulator = theano.function([inc],state,updates=[(state,state+inc)])
#print(accumulator(10))
#print(accumulator(10))

# to get variable value
print(state.get_value())
accumulator(1)
print(state.get_value())
accumulator(10)
print(state.get_value())

# to set varuable value
state.set_value(-1)
accumulator(3)
print(state.get_value())

# temporarily replace shared variable with another value in annother function
temp_function = state * 2 +inc
a = T.scalar(dtype=state.dtype)
skip_shared = theano.function([inc,a],temp_function,givens=[(state,a)])
print(skip_shared(2,3))
print(state.get_value())


