#!/usr/bin/python
#
#Time:2016-07-08
#Author:William
#Exercixe:5.17

import  random as rd

randint= rd.randint(1,100);
list=range(randint);
for i in range(randint):
    list[i]=rd.randint(0,2**31-1);
print randint;
print list;
list.sort();
print list;


