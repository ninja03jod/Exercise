Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s = '6+8j 90'
>>> s
'6+8j 90'
>>> s[0]
'6'
>>> s[1:5]
'+8j '
>>> s[1] = '-'
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    s[1] = '-'
TypeError: 'str' object does not support item assignment
>>> range(len(s))
range(0, 7)
>>> a = 'saad'
>>> a = 'saad is a good'
>>> s
'6+8j 90'
>>> a
'saad is a good'
>>> 
>>> a.capitalize()
'Saad is a good'
>>> a.split()
['saad', 'is', 'a', 'good']
>>> a.split()[-3]
'is'
>>> a.split()[-3] = 'was'
>>> a
'saad is a good'
>>> a.find(a)
0
>>> a.find('a')
1
>>> a.index('a')
1
>>> a.replace('saad','sakib')
'sakib is a good'
>>> print('-'.join(a))
s-a-a-d- -i-s- -a- -g-o-o-d
>>> print('-'.join(a.split()))
saad-is-a-good
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
