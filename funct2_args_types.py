""""""
"""
Q.what is advantage of function?
- code reusability
- We can write a code or function or declaration ones and call it for multiple times
=========================================
# We supply arguments in function

Arguments are of 4 types:
1) positional
2) keyword
3) default
4) variable length
-------------------------------
1) positional arguments:
In this arguments sequence order matters

Ex.
def info(height,weight):
    print(height,weight)
# call
info(6.2,68)
-----------------------------------
Ex.
def elig(per,backlog):
    print('percentage',per)
    print('backolgs',backlog)
# call
elig(3,89.85)
# The output shows the percentage = 3 & backlog = 89.85 
# Thus,sequence order matters in positional args 
----------------------------------------------------------
def elig(per,backlog):
    print('percentage: ',per)
    print('backolgs: ',backlog)
# call
elig(89.85,0)
============================================================================================
# we cant mixup the positional and keywords argument randomly
def info(bld_grp,height,weight):
    print('blood group',bld_grp)
    print('height',height)
    print('weight',weight)
    
#info(bld_grp='o-',6.3,65)*****************

# this calling is not accessible it shows syntax error
# bcauz we cant put first keyword args
# positional args does nt follow keywords args
# if we want to mix up positional and keyword then we have to give key=value at the end

info('o-',5.6,weight=52)*********************
============================================================================================
2) keyword argument:
- In keyword argument sequence order doesn't matters 
- At the time of calling fun we can put keywords = values

Ex.
def marks(grade1,grade2):
    print('Grade in maths',grade1)
    print('Grade in sci',grade2)
marks(grade2='A1',grade1='A2')
# we can execute the code or we can call the function by changing the position of keywords 
----------------------------------------------
Ex.
def info(name='saad',age=21):
    print('name:',name)
    print('age:',age)
info()
info('saurabh',23)
# we can supply the key=value in declaration also and
# at the time of calling the fun we put it blank so it will gives the output
# we can also manipulate the values for keywords at the time of calling
========================================================================================
3) Default arguments:
- when we want to set the value as a default value if not provided
- if we call new value then it takes it instead of default value
- it is an argument along with value in a declaration

Ex.
def add(num1=45,num2=65):
    print('Addition',num1+num2)
add() # o/p will be addition of 45+65
add(87,98) # changes default value
---------------------------------------------
Ex.
def oddeve(num1=43):
    if num1 %2 ==0:
        return 'even'
    else:
        return 'odd'
#print(oddeve()) # o/p will be odd
# lets change the default value
print(oddeve(32)) #o/p will be even
================================================================
4) variable length argument:
- Used to supply n number of values only to the arguments
- by using * as a prefix we can make the arguments 
Ex.
def num(*n):
    print(n)
num() # o/p shows only blank tuple
num(12,45,789,98,65,32) # o/p will be in tuple only values
----------------------------------------------
Ex.
# def add(*m,*n) it not takes multiple parameters
def add(*a):
    print(a)
add()
add(45,12,30)
=====================================================================
# varible length positional arguments = *args # shows values only
# variable length keywords arguments = **kywrds # shows the key=value
Ex.
def dic(**k):
    print(k)
dic(name='saad',age=22,height=5.6) # output will get in dictionary format as {key:value}
===================================================================================================
# positional arguments:
- In positional arguments sequence order matters
- Positional arguments allows the values in sequence of order while calling the function

# keyword arguments:
- In keyword arguments sequence of order does not matters
- We cn call the function by changing the position of keywords by providing them value

# default arguments:
- We want to set some value as a default for a particular keyword if not provided and if we put new value in args while calling fun
it allows the value instead of default value

# variable length argument:
# what is *args and **kwargs
# *args vs **kwargs

- *args used at prefix when we declaring the function 
- *args allows to accept n numbers of positional args
- o/p will get in tuple form
- while calling the function we are able to put n numbers of positional values only 

- **kwargs used at prefix while declaring the function
- **kwargs allows to accept keyword arguments
- o/p will get in dictionary
- while calling the function we are able to written keywords and their values
======================================================================================================================   

# positional vs kewyword

- positional args matters the sequence or order,whereas keyword args does not matter
- we can change the position of keyword=value and get the output , whereas in positional args we have to put values as
per sequence of order.
- while calling the function keyword args before positional args shows the error this is invalid 
for valid method we have put first positional args after that keyword args will shows o/p  
     
"""

































