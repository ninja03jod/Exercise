Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # list methods
>>> # features
>>> # background data structure is array
>>> # array is a contigous memory block
>>> # slicing and indexing done
>>> # list is mutable data type we can change the objects
>>> # list accpets the homo and hetro data
>>> # list preserves sequence order
>>> a = [10,40,'6+8j',10,30,'python',25,'saad',21,25]
>>> a
[10, 40, '6+8j', 10, 30, 'python', 25, 'saad', 21, 25]
>>> # indexing
>>> a[40]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a[40]
IndexError: list index out of range
>>> a[7]
'saad'
>>> a[-5]
'python'
>>> # slicing
>>> # creates new list means we can access the list from new start and stop
>>> # stop is exclusive means if we give the index at stop position then it won't be part of our output
>>> a
[10, 40, '6+8j', 10, 30, 'python', 25, 'saad', 21, 25]
>>> a[2:8]
['6+8j', 10, 30, 'python', 25, 'saad']
>>> a[-9:-3]
[40, '6+8j', 10, 30, 'python', 25]
>>> # we can change the objects by using index
>>> a[3] = 'java'
>>> a
[10, 40, '6+8j', 'java', 30, 'python', 25, 'saad', 21, 25]
>>> # lets see the list methods
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> a
[10, 40, '6+8j', 'java', 30, 'python', 25, 'saad', 21, 25]
>>> x = a.copy()
>>> x
[10, 40, '6+8j', 'java', 30, 'python', 25, 'saad', 21, 25]
>>> y = a
>>> y
[10, 40, '6+8j', 'java', 30, 'python', 25, 'saad', 21, 25]
>>> # x is shallow copy and y is deep copy
>>> # shallow copies have same elements but id's are different
>>> # deep copies have same elements and their id's
>>> x
[10, 40, '6+8j', 'java', 30, 'python', 25, 'saad', 21, 25]
>>> y
[10, 40, '6+8j', 'java', 30, 'python', 25, 'saad', 21, 25]
>>> x[5] = 456
>>> x
[10, 40, '6+8j', 'java', 30, 456, 25, 'saad', 21, 25]
>>> a
[10, 40, '6+8j', 'java', 30, 'python', 25, 'saad', 21, 25]
>>> # their no change happens in a due to x has its own file so this is a sahllow copy
>>> y[5] = 'bagwan'
>>> y
[10, 40, '6+8j', 'java', 30, 'bagwan', 25, 'saad', 21, 25]
>>> a
[10, 40, '6+8j', 'java', 30, 'bagwan', 25, 'saad', 21, 25]
>>> # changes are done in a and y both have same id and objects thas why this is a deep copy
>>> id(x)
1641213830856
>>> id(a)
1641208746184
>>> id(y)
1641208746184
>>> #=========================
>>> # append method
>>> a
[10, 40, '6+8j', 'java', 30, 'bagwan', 25, 'saad', 21, 25]
>>> a.append = 100
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a.append = 100
AttributeError: 'list' object attribute 'append' is read-only
>>> a.append(100)
>>> a
[10, 40, '6+8j', 'java', 30, 'bagwan', 25, 'saad', 21, 25, 100]
>>> a.append('c++')
>>> a
[10, 40, '6+8j', 'java', 30, 'bagwan', 25, 'saad', 21, 25, 100, 'c++']
>>> # append adds the objects by default at the end
>>> #==================
>>> # extend method
>>> a
[10, 40, '6+8j', 'java', 30, 'bagwan', 25, 'saad', 21, 25, 100, 'c++']
>>> # extend method can add the seperate elements inlist
>>> a.extend(200)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    a.extend(200)
TypeError: 'int' object is not iterable
>>> a.extend('hello')
>>> a
[10, 40, '6+8j', 'java', 30, 'bagwan', 25, 'saad', 21, 25, 100, 'c++', 'h', 'e', 'l', 'l', 'o']
>>> a.extend('200')
>>> a
[10, 40, '6+8j', 'java', 30, 'bagwan', 25, 'saad', 21, 25, 100, 'c++', 'h', 'e', 'l', 'l', 'o', '2', '0', '0']
>>> # extend adds seperate objects at the end
>>> #=============================================
>>> # insert method
>>> a
[10, 40, '6+8j', 'java', 30, 'bagwan', 25, 'saad', 21, 25, 100, 'c++', 'h', 'e', 'l', 'l', 'o', '2', '0', '0']
>>> # we can add object where ever we want in list means before this or after this
>>> a.insert(3,'sakib')
>>> a
[10, 40, '6+8j', 'sakib', 'java', 30, 'bagwan', 25, 'saad', 21, 25, 100, 'c++', 'h', 'e', 'l', 'l', 'o', '2', '0', '0']
>>> # we have to give the index and object by coma seperate then it will add
>>> # we can also add by negative index
>>> a.insert(-3,'numpy')
>>> a
[10, 40, '6+8j', 'sakib', 'java', 30, 'bagwan', 25, 'saad', 21, 25, 100, 'c++', 'h', 'e', 'l', 'l', 'o', 'numpy', '2', '0', '0']
>>> # suppose i have to add roz after sakib by positive index and sakib index number is 3 so we have to give index 4,'roz'
>>> # if we want the numpy before '2' by negative index and '2' is at index -3 so we have to give the exact that index for adding numpy
>>> #===============================
>>> # # count
>>> a
[10, 40, '6+8j', 'sakib', 'java', 30, 'bagwan', 25, 'saad', 21, 25, 100, 'c++', 'h', 'e', 'l', 'l', 'o', 'numpy', '2', '0', '0']
>>> a.count(0)
0
>>> a.count('0')
2
>>> a.count('l')
2
>>> # count gives the number that how many times this word or this word repeats 2 times
>>> #==================================
>>> # pop method
>>> a
[10, 40, '6+8j', 'sakib', 'java', 30, 'bagwan', 25, 'saad', 21, 25, 100, 'c++', 'h', 'e', 'l', 'l', 'o', 'numpy', '2', '0', '0']
>>> a.pop()
'0'
>>> a.pop()
'0'
>>> a.pop('2')
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    a.pop('2')
TypeError: 'str' object cannot be interpreted as an integer
>>> a.pop(100)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    a.pop(100)
IndexError: pop index out of range
>>> a.pop('2')[-1]
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    a.pop('2')[-1]
TypeError: 'str' object cannot be interpreted as an integer
>>> # pop will not takes any argument
>>> # pop removes an returns the object bydefault from last
>>> #===========================
>>> # remove method
>>> a
[10, 40, '6+8j', 'sakib', 'java', 30, 'bagwan', 25, 'saad', 21, 25, 100, 'c++', 'h', 'e', 'l', 'l', 'o', 'numpy', '2']
>>> a.remove()
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    a.remove()
TypeError: remove() takes exactly one argument (0 given)
>>> a.remove('2')
>>> a
[10, 40, '6+8j', 'sakib', 'java', 30, 'bagwan', 25, 'saad', 21, 25, 100, 'c++', 'h', 'e', 'l', 'l', 'o', 'numpy']
>>> a.remove(40)
>>> a
[10, '6+8j', 'sakib', 'java', 30, 'bagwan', 25, 'saad', 21, 25, 100, 'c++', 'h', 'e', 'l', 'l', 'o', 'numpy']
>>> a.remove('sakib')
>>> a
[10, '6+8j', 'java', 30, 'bagwan', 25, 'saad', 21, 25, 100, 'c++', 'h', 'e', 'l', 'l', 'o', 'numpy']
>>> # remove methods takes the one argument
>>> # it removes the specified objects what we want to remove from list if we dont give any argument then it raises error
>>> # ========================
>>> # pop vs remove
>>> # pop removes and returns the object,whereas remove does not retrns removed object it delets directly from list
>>> # pop will not take any argument,whereas remove takes one argument
>>> # pop is faster than remove because remove contain more method
>>> # pop raises index error while remove raises value error
>>> # pop removes objects bydefault from last,whereas remove method removes the specified object what we put inside
>>> #===============================
>>> # reverse method
>>> a
[10, '6+8j', 'java', 30, 'bagwan', 25, 'saad', 21, 25, 100, 'c++', 'h', 'e', 'l', 'l', 'o', 'numpy']
>>> a.reverse()
>>> a
['numpy', 'o', 'l', 'l', 'e', 'h', 'c++', 100, 25, 21, 'saad', 25, 'bagwan', 30, 'java', '6+8j', 10]
>>> # it reverse whole list
>>> #=========================
>>> # sort method
\
>>> a
['numpy', 'o', 'l', 'l', 'e', 'h', 'c++', 100, 25, 21, 'saad', 25, 'bagwan', 30, 'java', '6+8j', 10]
>>> # this methods sorts int to ascending to descending and chr or words into alphabetically
>>> x = [10,50,45,78,30,10,50,45,20,30,476,786]
>>> x
[10, 50, 45, 78, 30, 10, 50, 45, 20, 30, 476, 786]
>>> x.sort()
>>> x
[10, 10, 20, 30, 30, 45, 45, 50, 50, 78, 476, 786]
>>> # ascending to descending order
>>> y = ['saad','saqlain','umar','huzefa','ashraf','ibrahim']
>>> y
['saad', 'saqlain', 'umar', 'huzefa', 'ashraf', 'ibrahim']
>>> y.sort()
>>> y
['ashraf', 'huzefa', 'ibrahim', 'saad', 'saqlain', 'umar']
>>> # we can reveres this
>>> x.sort(reverse=True)
>>> x
[786, 476, 78, 50, 50, 45, 45, 30, 30, 20, 10, 10]
>>> y.sort(reverse=True)
>>> y
['umar', 'saqlain', 'saad', 'ibrahim', 'huzefa', 'ashraf']
>>> # we can sort words only on basis of their length
>>> y
['umar', 'saqlain', 'saad', 'ibrahim', 'huzefa', 'ashraf']
>>> y.sort(key=len)
>>> y
['umar', 'saad', 'huzefa', 'ashraf', 'saqlain', 'ibrahim']
>>> # we can reverse it also
>>> y.sort(key=len,reverse=True)
>>> y
['saqlain', 'ibrahim', 'huzefa', 'ashraf', 'umar', 'saad']
>>> #==============
>>> # clear
>>> x
[786, 476, 78, 50, 50, 45, 45, 30, 30, 20, 10, 10]
>>> x.clear()
>>> x
[]
>>> 
