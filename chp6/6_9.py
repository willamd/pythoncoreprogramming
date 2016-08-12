#!/usr/bin/python
#
#Time:2016-07-10
#Author:William
#Exercixe:6.9
str_input=raw_input("enter a string:>");
length=len(str_input);
result="";
for i in range(0,length):
    if str_input[i].islower():
        result+=str_input[i].upper();
    else:
        result+=str_input[i].lower();
print result;
