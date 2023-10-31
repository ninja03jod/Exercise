Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print()

>>> a = (10,20,30)
>>> a
(10, 20, 30)
>>> max(a)
30
>>> min(a)
10
>>> print(a,sep='\n')
(10, 20, 30)
>>> print(a, sep='-')
(10, 20, 30)
>>> print(10,20,30,sep = '-')
10-20-30
>>> print(10,20,30,sep = '\n')
10
20
30
>>> list(enumerate(a))
[(0, 10), (1, 20), (2, 30)]
>>> set(enumerate(a))
{(2, 30), (0, 10), (1, 20)}
>>> # chr to number and number chr conversion
>>> chr('A')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    chr('A')
TypeError: an integer is required (got type str)
>>> # no to chr and chr to number
>>> chr(65)
'A'
>>> chr(189)
'½'
>>> ord('a')
97
>>> ord('A')
65
>>> # ==========
>>> a = [1,2,3]
>>> a
[1, 2, 3]
>>> b = [4,5,6]
>>> b
[4, 5, 6]
>>> print(zip(a,b))
<zip object at 0x00000152FFFFFD48>
>>> dict(print(zip))
<class 'zip'>
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    dict(print(zip))
TypeError: 'NoneType' object is not iterable
>>> result = zip(a,b)
>>> result
<zip object at 0x00000152FFFFF848>
>>> dict.zip(a,b)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    dict.zip(a,b)
AttributeError: type object 'dict' has no attribute 'zip'
>>> dict.zip(result)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    dict.zip(result)
AttributeError: type object 'dict' has no attribute 'zip'
>>> print(zip(result))
<zip object at 0x00000152FFFFF7C8>
>>> print(dict(result))
{1: 4, 2: 5, 3: 6}
>>> x = [40,20,10]
>>> x
[40, 20, 10]
>>> y = [50,90,70]
>>> y
[50, 90, 70]
>>> q = zip(x,y)
>>> q
<zip object at 0x00000152FFFFF7C8>
>>> print(dict(q))
{40: 50, 20: 90, 10: 70}
>>> # =======================
>>> # frozenset
>>> # background data structure is hashtable
>>> # frozen set deoes not allow duplicates
>>> a = {1,4,5,6,2,3,1,5,2,3,1,8,7,4,1,2,3,4,65,8,6,4,7,9,1,2,3}
>>> a
{1, 2, 3, 4, 5, 6, 7, 8, 65, 9}
>>> frozenset(a)
frozenset({1, 2, 3, 4, 5, 6, 7, 8, 65, 9})
>>> # preserves sequence order
>>> b = {'saad',5,4,2,1,5,'python','4+9i'}
>>> b
{1, 2, 4, 5, '4+9i', 'saad', 'python'}
>>> frozenset(b)
frozenset({1, 2, 'python', 4, 5, '4+9i', 'saad'})
>>> # it does not preserve sequence order***************
>>> # frozenset is immutable we cant change it
>>> # acceptsb homo and hetro data
>>> # ================================
>>> # difference set and frozenset
>>> # frozenset has same features as set but set is mutable
>>> # frozenset is immutable
>>> # if we need to kep data private then we can use frozenset
>>> # if we want changes then set will be used
>>> # define frzenset*****
>>> # frozenset is an immutable version of built in function python
>>> # we cannot changes the elements of frozenset and such as we keep them private
>>> # ===========
>>> # input
>>> a = input('enter your name=')
enter your name='saad'
>>> a
"'saad'"
>>> per = float(input('eneter your percentage:'))
eneter your percentage:92.80
>>> per
92.8
>>> # ===============================
>>> 
