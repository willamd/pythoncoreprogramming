#!/usr/bin/python
#
#Time:2016-07-08
#Author:William
#Exercixe:5.15

def GCD(a,b):
    if str(a).isdigit() and str(b).isdigit():
        if a>b:
            if a%b==0:
                print "The max gys is",b;
                return b;
            else:
                c=a%b;
                return GCD(b,c);
        else:
            if b%a==0:
                print "the max gys is",a;
                return a
            else:
                c=b%a;
                return GCD(b, c);
    else:
        print "Data type error."
def LCD(a,b):
    if str(a).isdigit() and str(b).isdigit():
        if a>=b:
            if a%b==0:
                print "The least is",a;
                return a;
            else:
                gcd=GCD(a,b);
                return b/gcd*a;
        else:
            if b%a==0:
                print "The least is",b;
                return b;
            else:
                gcd=GCD(a,b);
                return a / gcd * b;






GCD(12,5);
GCD(12,'a');
GCD(12,4);
print LCD(12,6);
print LCD(12,5);
print LCD(6,8);
print LCD(3,4);