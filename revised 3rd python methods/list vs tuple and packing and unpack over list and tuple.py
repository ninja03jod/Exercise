Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # list vs tuple
>>> a = [10,50,'saad',45,'python',12,32,'java',10,54,21,45,6+8l]
SyntaxError: invalid syntax
>>> a = [10,50,'saad',45,'python',12,32,'java',10,54,21,45,'6+8l']
>>> a
[10, 50, 'saad', 45, 'python', 12, 32, 'java', 10, 54, 21, 45, '6+8l']
>>> b = (10,'saad',50,45,'python',12,45,10,'java')
>>> b
(10, 'saad', 50, 45, 'python', 12, 45, 10, 'java')
>>> # difference
>>> # list is mutable we can change the elements of list
>>> # tuple is immuatble we cannot change the elements
>>> # if we want to keep the data private then we use the tuple
>>> # if we need to change the objects then we go through the list
>>> # tuple is faster than list
>>> # list is slower cause it contains more method
>>> a
[10, 50, 'saad', 45, 'python', 12, 32, 'java', 10, 54, 21, 45, '6+8l']
>>> a[5] = 'karad'
>>> a
[10, 50, 'saad', 45, 'python', 'karad', 32, 'java', 10, 54, 21, 45, '6+8l']
>>> b[5] = 'kolhapur'
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    b[5] = 'kolhapur'
TypeError: 'tuple' object does not support item assignment
>>> # ==============================================================================
>>> # packing and unpacking over list and tuple
>>> a = [10,20,30]
>>> a
[10, 20, 30]
>>> # this is the packing of list means it access through one varible
>>> a1,a2,a3 = a
>>> a1
10
>>> a2
20
>>> a3
30
>>> # this above case is unpacking every element has seperate variable
>>> #================
>>> a = (45,50,60)
>>> a
(45, 50, 60)
>>> a1,a2,a3 = a
>>> a1
45
>>> a2
50
>>> a3
60
>>> # packing anmd unpacking over tuple
