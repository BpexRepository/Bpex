# Copyright (c) Microsoft Corporation 2015

from z3 import *
init('libz3.so')

x = Real('x')
y = Real('y')
s = Solver()
s.add(x + y > 5, x > 1, y > 1)
print(s.check())
print(s.model())
