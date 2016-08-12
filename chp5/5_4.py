#!/usr/bin/python
#
#Time:2016-07-08
#Author:William
#Exercixe:5.4

def rn(year):
    if year%4==0 and year%100!=0:
        print "rn";
    elif year %400==0:
        print "rn";
    else:
        print 'pn';
year=raw_input("Enter a year:>");
if year.isdigit():
    rn(int(year));
else:
    print "wrong data type"