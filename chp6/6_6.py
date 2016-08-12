#!/usr/bin/python
#
#Time:2016-07-10
#Author:William
#Exercixe:6.6

def strip(str1):
    length=len(str1)-1;
    index=0;
    while True:
        if str1[index]==' ':
            index+=1;
        else:
            break;
        if str1[length]==' ':
            length-=1;
        else:
            break;
    print str1[index:length];
strip(" dlc    ");