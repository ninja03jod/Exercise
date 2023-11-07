""""""
"""
Modules :
Module is a file,python file
extension - sample.py

module is container which to holds all programming things

using modular programming approach one can access members of other module
It means we create user defined module or file so we can access members or function we used 
in created file into other module or file 

There r 2 types of modules:

- built-in modules
- user defined modules
====================================
# Built-in modules
# Ex. math
import math
print(math.pi)
print(math.cos(45))
print(math.sqrt(144))
---------------------------------------
# let's skip the name and directly we can add methods or functions
from math import *
print(factorial(8))
print(tau)
print(degrees(23))
------------------------------------------------
# Module aliasing : Giving a short name or nick name to a module
import math as m
print(m.pi)
print(m.factorial(4))
print(m.sqrt(1440))
----------------------------------
# we can specify the members of modules means we use only those functions what we import
from math import pi,sqrt,factorial
print(factorial(89))
print(sqrt(49))
--------------------------------------
# Member alaising : giving a nick name to members of modules
from math import factorial as f,sqrt as s,pi as p
print(f(8))
print(p)
print(s(8))
======================================
from math import *
x = 49
y = 100
d = sqrt(x**2+y**2)
print(d)

r = 5
area = floor(pi*r**2)
print(area)

======================================
import math 
from math import*
module alaising - import math as m
from math import factorial,sqrt,...
member alaising - from math import factorial as f,sqrt as s,....
===================================================================
# what is module: module is file , python file
module is a container which brings all programming things
By using module approach one can access the members of other module

# Difference between import math and from math import *
- In import math we can access the members of module math by printing (math.member/var)
- from math import * in this case we can access the members directly without using name (math.)
- import math is slower as compare to import * 

# module aliasing: Giving short name to the module like 
import math as m (This will saves the time & code will be simple and short)

# member aliasing : Giving short name to the members of module like 
from math import factorial as f,sqrt as s,pi as p... 
(This will saves the time & code will be simple and short)
"""












