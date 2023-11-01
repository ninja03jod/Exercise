""""""
"""
def posneg(a):
    if a >= 0:
        return '+ve'
    else:
        return '-ve'

a1 = posneg(5)
# print(a1)
if a1 == '-ve':
    print('temperature is cold')
else:
    print('temperature is not too much cold')
===================================================
# write a function to return the even or odd number
def even(num):
     if num %2 ==0:
         return 'even number'
     else:
         return 'odd number'
num = int(input('enter number: '))
print(even(num))
==============================================

# write a function to return the even , odd or -ve number
def even(num):
     if num %2 ==0:
         return 'even number'
     elif num < 0:
         return '-ve number'
     else:
         return 'odd number'
num = int(input('enter number: '))
print(even(num))
=========================================
# write a function to return the square of num
def sq(num):
    num = 10
    return num**2
#print(sq(10))
a1 = sq(10)
if a1 == 100:
    print('yes')
else:
    print('no')
============================================================

# write a function to return the num is divisible by 5 , not divisble by 2 or divisible by 2
def div(num):
    if num %5 == 0:
        return 'divisible by 5'
    elif num %2 != 0:
        return 'not divisible by 2'
    else:
        return 'divisible by 2'
print(div(98))
print(div(73))
print(div(46))
print(div(3))
print(div(50))
=====================================================

def div(num):
    if num %5 == 0:
        return 'divisible by 5'
    elif num %2 != 0:
        return 'not divisible by 2'
    else:
        return 'divisible by 2'
x = div(23)
if x == 'not divisible by 2':
    print(23,'is odd number')
else:
    print('none')
o/p = 23 is odd number
"""
