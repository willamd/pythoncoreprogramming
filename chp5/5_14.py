#!/usr/bin/python
#
#Time:2016-07-08
#Author:William
#Exercixe:5.14

def bank_rate(rate):
    print (1.+rate)**365-1;
rate=raw_input("Enter the rate of bank,After a year:");
rate_value=eval(rate);
bank_rate(rate_value);