#code
import math
from math import ceil
def add(s1,s2):
    s1=s1[::-1] 
    s2=s2[::-1] 
    s=""
    c=0
    for i in range(max(len(s1) , len(s2))):
        f=0
        sc=0
        if i<len(s1):
            f=int(s1[i])
        if i<len(s2):
            sc = int(s2[i])
        
        o = f +sc + c
        # print(o)
        if(o==1 or o==3):
            s+="1"
        if(o==0 or o==2):
            s+="0"
        if(o==0 or o==1):
            c=0
        if(o==2 or o==3):
            c=1
    # print(c)
    if(c==1):
        s+="1"
    s=s[::-1]
    return s

def make_lens_equal(s1,s2):
    if(len(s1) == len(s2)):
        return [s1,s2]
    
    n1=len(s1)
    n2=len(s2)
    if(n1>n2):
        s2="0"*(n1-n2)+ s2
    else:
        s1="0"*(n2-n1) + s1
    return [s1,s2]
    
def shift(s , n):

    return s + "0"*n
def multiply(s1,s2):
    l = make_lens_equal(s1,s2)
    s1=l[0]
    s2=l[1]
    if(len(s1) == 1):
        return ((int(s1[0]))*int(s2[0]))

    n=len(s1)
    xl = s1[0:int(n/2)]
    xr = s1[int(n/2):]
    yl = s2[0:int(n/2)]
    yr = s2[int(n/2):]

    xlyl = multiply(xl , yl)
    xryr = multiply(xr , yr)
    # print(s1,s2 , xlyl , xryr , xl,yr , add(xl,yr) , add(xr,yl))

    thesumthing = multiply( add(xl,xr) , add(yl , yr)) - xlyl - xryr
    # print(s1,s2, thesumthing)
    answer = pow(2,n)*xlyl + pow(2,ceil(n/2)) * thesumthing + xryr
    # print(answer)
    return int(answer)

print(multiply("1010" , "1001"))

