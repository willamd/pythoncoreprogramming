#!/usr/bin/python
#
#Time:2016-07-10
#Author:William
#Exercixe:6.3

list=[];
print "Input Q to quit"
while True:
    input_value=raw_input("Enter a element:>");
    if input_value!='Q':
        list.append(input_value);
    else:
        break;
list.sort();
print list;

value_list=raw_input("Enter a list of number:>");
list_append=[];
temp=value_list.split(' ');
for i in temp:
    list_append.append(i);
print list_append;
list_append.sort();
print list_append;
