#!/usr/bin/python
#
#Time:2016-07-08
#Author:William
#Exercixe:5.3

import types

print "Input any str to quit"
while True:
    input_str=raw_input("Enter the scole of the Student:>");
    #print type(input_str)
    #print input_str.isalnum()
    if input_str.isdigit():#type(input_str) == types.StringType:
        get_input=int(input_str);
        if get_input>=90 and get_input<=100:
            print "A";
        elif get_input >= 80 and get_input <= 89:
            print "B";
        elif get_input >= 70 and get_input <= 79:
            print "C";
        elif get_input >=60 and get_input <= 69:
            print "D";
        else:
            print "F";
    else:
        print "The data type is wrong.";
        break;