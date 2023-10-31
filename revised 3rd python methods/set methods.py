Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # set and its methods
>>> # features
>>> # background data str is hash table means no array,no indexind and slicing
>>> # # set does not allows duplicates
>>> # set accpets home and hetro data
>>> # set is mutable we can add update remove the objects fromit
>>> a = set()
>>> a
set()
>>> type(a)
<class 'set'>
>>> s = {10,50,45,12,35,10,12,10,45,85,67,67,64,344,4153}
>>> s
{64, 35, 67, 10, 12, 45, 50, 85, 344, 4153}
>>> # removes the duplicates
>>> # add method
>>> s
{64, 35, 67, 10, 12, 45, 50, 85, 344, 4153}
>>> s.add(100)
>>> s
{64, 35, 67, 100, 10, 12, 45, 50, 85, 344, 4153}
>>> s.add('python')
>>> s
{64, 35, 67, 100, 'python', 10, 12, 45, 50, 85, 344, 4153}
>>> # it adds the objects where ever they want
>>> # =========================================
>>> # update
>>> s
{64, 35, 67, 100, 'python', 10, 12, 45, 50, 85, 344, 4153}
>>> s.update({258,320,456})
>>> s
{64, 320, 258, 35, 67, 100, 'python', 456, 10, 12, 45, 50, 85, 344, 4153}
>>> # update can add multiple objects is set
>>> s.add()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    s.add()
TypeError: add() takes exactly one argument (0 given)
>>> # ==========================================
>>> # intersection
>>> s
{64, 320, 258, 35, 67, 100, 'python', 456, 10, 12, 45, 50, 85, 344, 4153}
>>> a = {67,100,'java',456,'python',741,852,963}
>>> a
{67, 'java', 100, 'python', 741, 456, 963, 852}
>>> s.intersection(a)
{'python', 67, 100, 456}
>>> # it gives the common elements from both set
>>> s
{64, 320, 258, 35, 67, 100, 'python', 456, 10, 12, 45, 50, 85, 344, 4153}
>>> a
{67, 'java', 100, 'python', 741, 456, 963, 852}
>>> # it return the copy of set can't change the original set
>>> #=========================
>>> # difference
>>> s
{64, 320, 258, 35, 67, 100, 'python', 456, 10, 12, 45, 50, 85, 344, 4153}
a
>>> 
>>> a
{67, 'java', 100, 'python', 741, 456, 963, 852}
>>> s.difference(a)
{64, 320, 258, 35, 10, 12, 45, 50, 85, 344, 4153}
>>> # it gives the uncommon element from set 1 only
>>> s
{64, 320, 258, 35, 67, 100, 'python', 456, 10, 12, 45, 50, 85, 344, 4153}
>>> # it can't change the original set it returns the copy
>>> a.difference(s)
{963, 'java', 741, 852}
>>> # ====================
>>> # symmetric_difference
>>> s
{64, 320, 258, 35, 67, 100, 'python', 456, 10, 12, 45, 50, 85, 344, 4153}
>>> a
{67, 'java', 100, 'python', 741, 456, 963, 852}
>>> s.symmetric_difference(a)
{64, 320, 258, 963, 'java', 10, 12, 852, 85, 344, 35, 741, 45, 50, 4153}
>>> s
{64, 320, 258, 35, 67, 100, 'python', 456, 10, 12, 45, 50, 85, 344, 4153}
>>> # this will gives the uncommon element from both set and it will returns the copy
>>> # ==========================
>>> # symmetric_difference_update
>>> s
{64, 320, 258, 35, 67, 100, 'python', 456, 10, 12, 45, 50, 85, 344, 4153}
>>> a
{67, 'java', 100, 'python', 741, 456, 963, 852}
>>> s.symmetric_difference_update(a)
>>> s
{64, 320, 258, 35, 'java', 963, 741, 10, 12, 45, 50, 852, 85, 344, 4153}
>>> s
{64, 320, 258, 35, 'java', 963, 741, 10, 12, 45, 50, 852, 85, 344, 4153}
>>> # it gives the uncommon elements from both sets and it will change the original set
>>> c = {32,1654,987,123,654,5421,34,10,12,'java','python','c++'}
>>> 
>>> c
{32, 34, 'java', 'python', 987, 'c++', 10, 12, 5421, 654, 1654, 123}
>>> s.symmetric_difference_update(c)
>>> s
{258, 654, 32, 34, 35, 45, 5421, 50, 4153, 64, 320, 963, 'c++', 852, 85, 344, 987, 'python', 741, 1654, 123}
>>> c
{32, 34, 'java', 'python', 987, 'c++', 10, 12, 5421, 654, 1654, 123}
>>> s
{258, 654, 32, 34, 35, 45, 5421, 50, 4153, 64, 320, 963, 'c++', 852, 85, 344, 987, 'python', 741, 1654, 123}
>>> # it changes the original set
>>> # ===============================
>>> # union
>>> a
{67, 'java', 100, 'python', 741, 456, 963, 852}
>>> c
{32, 34, 'java', 'python', 987, 'c++', 10, 12, 5421, 654, 1654, 123}
>>> a.union(c)
{67, 'java', 963, 'c++', 456, 10, 12, 654, 852, 987, 32, 34, 100, 'python', 741, 5421, 1654, 123}
>>> # it add and returns the both set into one
>>> # ==========================
>>> # intersection_upddate
>>> s
{258, 654, 32, 34, 35, 45, 5421, 50, 4153, 64, 320, 963, 'c++', 852, 85, 344, 987, 'python', 741, 1654, 123}
>>> a
{67, 'java', 100, 'python', 741, 456, 963, 852}
>>> c
{32, 34, 'java', 'python', 987, 'c++', 10, 12, 5421, 654, 1654, 123}
>>> a.intersection_update(c)
>>> a
{'python', 'java'}
>>> # fetches the common element
>>> s.intersection_update(a)
>>> s
{'python'}
>>> # it chngaes the orginal set
>>> s
{'python'}
>>> a
{'python', 'java'}
>>> c
{32, 34, 'java', 'python', 987, 'c++', 10, 12, 5421, 654, 1654, 123}
>>> # ==========================
>>> x = c.copy()
>>> x
{32, 34, 'java', 'python', 987, 'c++', 10, 12, 5421, 654, 1654, 123}
>>> y = c
>>> y
{32, 34, 'java', 'python', 987, 'c++', 10, 12, 5421, 654, 1654, 123}
>>> # above case is copy method
>>> id(x)
2465938094792
>>> id(c)
2465938095688
>>> id(y)
2465938095688
>>> # x is shallow copy and y is deep copy
>>> # =======================================
>>> # pop
>>> s
{'python'}
>>> x
{32, 34, 'java', 'python', 987, 'c++', 10, 12, 5421, 654, 1654, 123}
>>> y
{32, 34, 'java', 'python', 987, 'c++', 10, 12, 5421, 654, 1654, 123}
>>> a
{'python', 'java'}
>>> x.pop()
32
>>> x.pop()
34
>>> # pop removes and returns the randomelements from set
>>> x.pop('python')
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    x.pop('python')
TypeError: pop() takes no arguments (1 given)
>>> # =============================
>>> # remove
>>> x
{'java', 'python', 987, 'c++', 10, 12, 5421, 654, 1654, 123}
>>> y
{32, 34, 'java', 'python', 987, 'c++', 10, 12, 5421, 654, 1654, 123}
>>> s
{'python'}
>>> a
{'python', 'java'}
>>> x.remove('java')
>>> x
{'python', 987, 'c++', 10, 12, 5421, 654, 1654, 123}
>>> s.remove(4751)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    s.remove(4751)
KeyError: 4751
>>> y.remove(32)
>>> y
{34, 'java', 'python', 987, 'c++', 10, 12, 5421, 654, 1654, 123}
>>> # it removes the element direct fromlist without returns
>>> # remove takes one argument
>>> # if value is not present in the set then it raises key error
>>> # =============================
>>> # discard
>>> x
{'python', 987, 'c++', 10, 12, 5421, 654, 1654, 123}
>>> y
{34, 'java', 'python', 987, 'c++', 10, 12, 5421, 654, 1654, 123}
>>> x.discard()
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    x.discard()
TypeError: discard() takes exactly one argument (0 given)
>>> # discard takes one argument
>>> x.discard('python')
>>> x
{987, 'c++', 10, 12, 5421, 654, 1654, 123}
>>> # discard also not returns the removed element it directly delets from the set
>>> # when no argument is given then it raises error
>>> x.discard(78945)
>>> 
>>> # if the value given is not avail in set then it will do nothing
>>> # ===================================
>>> # difference pop,remove and discard
>>> # pop removes and returns the element
>>> # whereas remove and discard does not returns removed element it delets fromthe set
>>> 
>>> # pop will not take any argument
>>> # whereas remove and discard takes one argument
>>> 
>>> # pop removes random element from set
>>> # whereas remove and discard removes spcified element
>>> 
>>> # pop raises error when we give argument
>>> # removes raises error if given argument is not avail in set
>>> # discard raises error when the no argument is given and if given argument is not avail in set then it will do nothing
>>> 
>>> # ======================================
>>> x
{987, 'c++', 10, 12, 5421, 654, 1654, 123}
>>> x.clear()
>>> x
set()
>>> # pop is fatser than remove and discard
>>> # =========================================
>>> dir(set)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> 
