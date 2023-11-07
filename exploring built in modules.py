""""""
""
# random

# import random
print(random.randint(20,89)) # rand it gives the random int between range 20-89
print(random.randint(-98,-1))
print(random.choice(['sAad','sakib','umar'])) # this choices the random element from sequence
print(random.choice(['sakib','akib','abu','amir']))
print(random.choice([45,65,233,655])) # this choices the random int from sequence
==================================
# from random import *
print(randint(-1,85))
print(choice(['anuj','rushikesh','pratik']))
====================================
# module aliasing
import random as r
print(r.choice([45,87,98,12]))
print(r.randint(1,10))
====================================
# specify the members of module
from random import randint,choice
print(randint(65,68))
print(choice(['saad','javed','bagwan']))
==========================================
# member aliasing
from random import randint as rt,choice as ce
print(rt(89,545))
print(ce(['a','t','s']))
===================================================
# import array
print(array.ArrayType('i',[89,54]))

# ArrayType member of array module gives 'i' as int value

print((array.ArrayType('f',[78.23,5.3])))
# ArrayType member of array module gives 'f' as floating value
-----
import array
print(array.ArrayType('u',['A','v','I']))
# type code 'u' as str can access unicode chr

print(array.ArrayType('q',[78,89,95]))
# some specified type codes are same for int,float and str
==============================================================
from array import ArrayType
print(ArrayType('q',[78,98,65,32,12]))
=========================================
from array import ArrayType
print(ArrayType('f',[6.5,3.2,1.0]))
========================================
import array as a
print(a.ArrayType('d',[6.3,55.2]))
=========================================
from array import ArrayType as at
print(at('u',['s','A','a','D']))
===================================
***************IMP
from array import *
str = array('u',['s','a','a','d'])
print(str.buffer_info())
# it gives address and size of chr 
================================
from array import *
int = array('i',[9,8,-9,8,4,3,2,-5,1])
# if we want to apply function then we have to use it and then write print
int.append(6)
print(int)
=================================
from array import *
num = array('i',[78,98,98,65])
num.extend([6,8])
print(num)
===================================

from array import *
str = array('u',['s','a','a','d'])

for i in range(4):
    print(str[i])
# this will iterate each element of str

from array import *
str = array('u',['s','a','a','d'])

for i in str:
    print(i)
-----------------
from array import *
str = array('u',['s','a','a','d'])
str.extend(['d','k'])
print(str)
# lets iterate on by one
for i in range(6):
    print(str[i])
----------------------------
from array import *
str = array('u',['s','a','A','D'])
str.extend(['i','k','l','m'])
print(str)
for i in str:
    print(i,end=' ')
==========================================
from array import *
str = array('i',[2,5,8,9,6])
newstr = array(str.typecode, (a*a for a in str))
for i in newstr:
    print(i)
# performs iteration with square     
---------------------------
from array import *
rem = array('i',[9,5,1,3,5,7])
rem.pop()
print(rem)
sq = array(rem.typecode, (i*i for i in rem))
for j in sq:
    print(j)
====================================
# collection

import collections
set2 = {8,8,6,3,8,4}
print(set2)
=================================
# time module
import time
print(time.time())
----------------------------
from time import *
lcl_tm= localtime()
print('local time is:',lcl_tm)
# it gives the current time with day, month,min,sec,yearly day form 365,hours
"""




















