""""""
"""
Assignment : check all operation you performed on if elif and else using function
def check(num):
    if num == 10:
        print('condition is true')
check(10)
=========================================
# we can test multiple condition in if
def mult(height,weight):
    if (height >= 6) and (weight <= 70):
        print('perfect')
height = float(input('enter height: '))
weight = float(input('enter weight: '))
mult(height,weight)
=============================================
# if else ex:
def mult(height,weight):
    if (height >= 6) and (weight <= 70):
        print('perfect')
    else:
        print('not good')
mult(5.4,59)
==========================================
# write a program to get 30% discount above 3000 price
def buyer(price):
    if (price >= 3000):
        print('Buyer will get 30% discount')
    else:
        print('price is under 3000')
buyer(2500)
buyer(3000)
buyer(4500)
===============================================
# if elif else in function:
# write a program to get the discount of 50% with firecrackers when purchasing price above 4500 and 
# rs 1000 extra clothes 
def customer(price,xtra_clts):
    if price>= 4500:
        print('Customer should buy xtra 1000 rs clothes to get 50% disc with firecrackers')
    if price <= 4500:
        print('price is under 4500')
    elif xtra_clts>= 1000:
        print('Customer gets the 50% discount with firecrackers')
    else:
        print('Customer not able to get disc')
price = int(input('enter price: '))
xtra_clts = int(input('enter extra buying price: '))
customer(price,xtra_clts)
==========================================================================================
# write a program for numbers which are divisble by 5 , not divisible by 2 and divisible by 2
def div(a):
    if a %5 ==0:
        print(a,'divisible by 5')
    elif a %2 != 0:
        print(a,'not divisbile by 2')
    else:
        print('divisble by 2')
a = int(input('enter number:'))
div(a)
================================================================
# elif ladder used in function
# write a program to check the grades of student
def temperature(temp):
    if temp >= 35:
        print('temperature is hot')
    elif temp >= 30:
        print('temperature is medium')
    elif temp >= 20:
        print('temperature is low')
    elif temp <= 20:
        print('temperature is cold')
temperature(37)
temperature(17)
temperature(-6)
temperature(24)
temperature(33)
temperature(3)
==============================================
# nested if in function
# eligibility criteria 
def elig(per,backlog):
    if per >= 70:
        if backlog <3:
            print('student is eligible to fill the form')
        else:
            print('student have more than 3 backlog')
    else:
        print('student not eligible')
per = float(input('enter percentage: '))
backlog = int(input('enter backlogs: '))
elig(per,backlog)
"""















