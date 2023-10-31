Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # dict
>>> # features
>>> # background data structure is hastable
>>> # dupliacte keys are not allowed but duplicate values are allowed
>>> # dict is mutable data type we can update the dictionary
>>> # ===========================
>>> a = {1:100,2:100,1:100}
>>> a
{1: 100, 2: 100}
>>> a[1] = 'python'
>>> a
{1: 'python', 2: 100}
>>> # we can change the elements of dict
>>> # keys method
\
>>> a
{1: 'python', 2: 100}
>>> a.keys()
dict_keys([1, 2])
>>> # values method
>>> a.values()
dict_values(['python', 100])
>>> # ===========================
>>> # get method
>>> a
{1: 'python', 2: 100}
>>> a.get()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a.get()
TypeError: get expected at least 1 arguments, got 0
>>> # get methods have to give one argument
>>> a
{1: 'python', 2: 100}
>>> a.get(2)
100
>>> a.get(3)
>>> 
>>> # in get method we access the values and it returns that values by usng keys
>>> # if we write the key which is not avail in the dict then it will do othing
>>> # =======================
>>> # update method
>>> a
{1: 'python', 2: 100}
>>> a.update({3:'java',4:400,5:'6+9i'})
>>> a
{1: 'python', 2: 100, 3: 'java', 4: 400, 5: '6+9i'}
>>> # we can add multiple key value pair in dict
>>> a.update(5,'c++')
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a.update(5,'c++')
TypeError: update expected at most 1 arguments, got 2
>>> a.update({5:'c++'})
>>> a
{1: 'python', 2: 100, 3: 'java', 4: 400, 5: 'c++'}
>>> # here is the option that only avail in dict
>>> # we can change the value of older key
>>> a.update({'mumbai'})
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.update({'mumbai'})
ValueError: dictionary update sequence element #0 has length 6; 2 is required
>>> # ============================
>>> # copy
>>> a
{1: 'python', 2: 100, 3: 'java', 4: 400, 5: 'c++'}
>>> x = a.copy()
>>> x
{1: 'python', 2: 100, 3: 'java', 4: 400, 5: 'c++'}
>>> y = a
>>> y
{1: 'python', 2: 100, 3: 'java', 4: 400, 5: 'c++'}
>>> # x is a shallow copy and y is a deep copy
>>> x.update({'mumbai':'marine drive'})
>>> x
{1: 'python', 2: 100, 3: 'java', 4: 400, 5: 'c++', 'mumbai': 'marine drive'}
>>> a
{1: 'python', 2: 100, 3: 'java', 4: 400, 5: 'c++'}
>>> y.update({'delhi':'capital'})
>>> y
{1: 'python', 2: 100, 3: 'java', 4: 400, 5: 'c++', 'delhi': 'capital'}
>>> a
{1: 'python', 2: 100, 3: 'java', 4: 400, 5: 'c++', 'delhi': 'capital'}
>>> # elements are same and id are different they are shallow copies
>>> # in y elemenst and ids are different thats why this is a deep copy
>>> id(a)
1783061753648
>>> id(x)
1783062581752
>>> id(y)
1783061753648
>>> # ==========================================
>>> # setdefault
>>> x
{1: 'python', 2: 100, 3: 'java', 4: 400, 5: 'c++', 'mumbai': 'marine drive'}
>>> y
{1: 'python', 2: 100, 3: 'java', 4: 400, 5: 'c++', 'delhi': 'capital'}
>>> a
{1: 'python', 2: 100, 3: 'java', 4: 400, 5: 'c++', 'delhi': 'capital'}
>>> a.setdefault()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a.setdefault()
TypeError: setdefault expected at least 1 arguments, got 0
>>> a.setdefault(5)
'c++'
>>> a.setdefault(8)
>>> a
{1: 'python', 2: 100, 3: 'java', 4: 400, 5: 'c++', 'delhi': 'capital', 8: None}
>>> # in setdefault method we can acces the values by using keys
>>> # in this method if we give the key which is not avail in dict then witll print that key inside dict with none value
>>> # difference between get setdefault and update
>>> # set default and get method need 1 argument
>>> # either they will generate error
>>> # if key is not present in the wich we give in get method then then it will do nothing
>>> # if same approach applies in setdefault method thenit will add that key wityh none value
>>> # ==========================================
>>> # pop
>>> a
{1: 'python', 2: 100, 3: 'java', 4: 400, 5: 'c++', 'delhi': 'capital', 8: None}
>>> a.pop()
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 arguments, got 0
>>> # in dict only pop takes an argument
>>> a.pop('mumbai')
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    a.pop('mumbai')
KeyError: 'mumbai'
>>> a.pop('delhi')
'capital'
>>> a
{1: 'python', 2: 100, 3: 'java', 4: 400, 5: 'c++', 8: None}
>>> # pop removes and returns the specified value of particular key
>>> a.pop(5)
'c++'
>>> a
{1: 'python', 2: 100, 3: 'java', 4: 400, 8: None}
>>> # ======================
>>> # popitem
>>> x
{1: 'python', 2: 100, 3: 'java', 4: 400, 5: 'c++', 'mumbai': 'marine drive'}
>>> x.popitem()
('mumbai', 'marine drive')
>>> x
{1: 'python', 2: 100, 3: 'java', 4: 400, 5: 'c++'}
>>> x.item()
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    x.item()
AttributeError: 'dict' object has no attribute 'item'
>>> # popitem removes and returns the key value pair
>>> x.popitem(2)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    x.popitem(2)
TypeError: popitem() takes no arguments (1 given)
>>> # popitem will not take any argument
>>> # popitemremoves randome key value pair
>>> # ==============
>>> # difference between pop and popitem
>>> # pop takes one argument,whereas popitem doesn't  takes any argument
>>> # pop removes and returns the specified value of particular key
>>> # popitem removes and returns the randomkey value pair
>>> # pop raises error when argument is given
>>> # popitem raises error when argument is given
>>> x.pop(1)
'python'
>>> x.pop(6)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    x.pop(6)
KeyError: 6
>>> x.pop(6,error)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    x.pop(6,error)
NameError: name 'error' is not defined
>>> a.pop(9,'error')
'error'
>>> # if we write a key which is not avail in dict then it will raises the error and if we dont want the error then we can write value after key by coma sperated
>>> # ==========================================
>>> # fromkeys
>>> # we can create new key value pair
>>> d = {}
>>> d
{}
>>> d.fromkeys([10,20,30])
{10: None, 20: None, 30: None}
>>> # it creats new key and values are same fro all keys
>>> d.fromkeys([10,20,30],500)
{10: 500, 20: 500, 30: 500}
>>> # =======================
>>> # clear
>>> s
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> a
{1: 'python', 2: 100, 3: 'java', 4: 400, 8: None}
>>> a.clear()
>>> a
{}
>>> 
