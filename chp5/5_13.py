#!/usr/bin/python
#
#Time:2016-07-08
#Author:William
#Exercixe:5.13

def hour_minute(a,b):
    print "After convert is",a*60+b;
time=raw_input("Input the time(HH:MM)>");
time_list=time.split(':');
hour=eval(time_list[0]);
minutes=eval(time_list[1]);
if (hour<0 or hour>23) and (minutes <0 or minutes>59):
    print "error.";
else:
    hour_minute(eval(time_list[0]),eval(time_list[1]))