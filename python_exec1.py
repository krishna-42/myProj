
import os

#Import the necessary packages

def sim_int(p,n,r):
    p=int(input(""))
    n=int(input(""))
    r=int(input(""))
    si =(p*n*r)/100
    print(f"The Simple Interest is {si}")
    print(dir())
    return si

import math
def ceil_floor(a,b):
    a=eval(input(""))
    b=eval(input(""))
    print(math.ceil(a))
    print(math.floor(b))
    return a,b

from math import sqrt
def lists():
    lst = []

    cnt_in=5
    while cnt_in >0:
        ele=float(input(""))
        lst.append(round(sqrt(int(ele)),2))
        cnt_in -=1
    print(lst)
    print(type(ele))
    return lst

# Driver code
