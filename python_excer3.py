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


def deg_rad():
    lst = []
    lst1 = []
    cnt = 5
    while cnt > 0:
        ele = int(input(""))
        lst.append(round(math.degrees(ele), 2))
        lst1.append(round(math.radians(ele), 2))
        cnt -= 1
    print(lst)
    print(lst1)


def strings():
    txt = input("")
    print(txt.swapcase())
    print(txt.title())
    print(txt.isidentifier())
    print(txt.zfill(50))


prof_loss()
