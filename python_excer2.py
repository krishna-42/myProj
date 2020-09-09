import os

def stringops():
    a=input("")
    a=a.strip()
    print(f"Enter a string: {a[2:4]}")
    print(a[-6:-3])
    print(len(a)+1)
    print(a.strip())
    print("", a.replace(a[4],"p"))
    print("", a.lower())

def stringopss():
    a=input("")
    print(f"Enter a string: {a.count(a[4])}")
    print(a.encode())
    print(a.isdigit())
    print(a.find("l",2,5))
    print(a.rfind("W"))

def listup():
    lst = []
    cnt = 5
    while cnt > 0:
        ele = int(input(""))
        lst.append(ele)
        cnt-=1
    print(lst[1::2])
    print(lst[::2])
    tup=tuple(lst)
    print(len(tup))
    tup=list(tup)
    tup[1]=5
    tup=tuple(tup)
    print(tup)

#stringops()
stringopss()
#listup()

import os
import math


# Python Program to Calculate Profit or Loss
def prof_loss():
    actual_cost = float(input(""))
    sale_amount = float(input(""))
    if sale_amount > actual_cost:
        print("Total Profit =", sale_amount - actual_cost)
    elif sale_amount < actual_cost:
        print("Total Loss =", actual_cost - sale_amount)
    else:
        print("No Profit No Loss!!!")

