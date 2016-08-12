#!/usr/bin/python
#
#Time:2016-07-08
#Author:William
#Exercixe:soft copy and deep copy

person=['name',['saving',100.0]];
"""hubby=person[:];
wifi=list(person);
print [id(x) for x in person,hubby,wifi];
hubby[0]='dlc';
wifi[0]='lc';
print hubby,wifi;
hubby[1][1]=50.0;
print hubby,wifi;"""

import copy
wifey=copy.deepcopy(person);
hubby=person;

wifey[0]='dlc';
hubby[0]='dd';
hubby[1][1]=50.0;
print '*'*10
print wifey;
print hubby;


