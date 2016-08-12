#!/usr/bin/python
#
#Time:2016-07-08
#Author:William
#Exercixe:5.11

def old(a,b):
    temp=a;
    while temp<=b:
        if temp %2==0:
            print temp;
        temp += 1;
def even(a,b):
    temp = a;
    while temp<=b:
        if temp %2==1:
            print temp;
        temp += 1;
old(0,20);
even(0,20);

def zc(a,b):
    if a>=b:
        if a%b==0:
            return True;
        else:
            return False;
    else:
        if b%a==0:
            return  True;
        else:
            return False;
print zc(2,4);
print zc(3,4);
