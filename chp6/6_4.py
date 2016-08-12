#!/usr/bin/python
#
#Time:2016-07-10
#Author:William
#Exercixe:6.5

import types

print "Input any str to quit"
list=[];
while True:
    input_str=raw_input("Enter the scole of the Student:>");
    #print type(input_str)
    #print input_str.isalnum()
    if input_str.isdigit():#type(input_str) == types.StringType:
        get_input=int(input_str);
        list.append(get_input);
    else:
        print "The data type is wrong.";
        break;

average=sum(list)*1.0/len(list);
print "The average score is:",average;