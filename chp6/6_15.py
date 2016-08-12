#coding=utf-8
#!/usr/bin/python
#
#Time:2016-07-11
#Author:William
#Exercixe:6.15
#The data convert;
import datetime as dt
def convert_date(date1,date2):
    date1_list=date1.split('/');
    date2_list=date2.split('/');
    date1_time=dt.date(int(date1_list[2]),int(date1_list[1]),int(date1_list[0]));
    date2_time=dt.date(int(date2_list[2]),int(date2_list[1]),int(date2_list[0]));
    days_num=abs(date1_time-date2_time);
    print days_num.days;
date1=raw_input("Enter a date:DD/MM/YY:>");
date2=raw_input("Enter another date:DD/MM/YY->");
convert_date(date1,date2);
def total_days(birthday):
    date1_list=birthday.split('/');
    date1_time=dt.date(int(date1_list[2]),int(date1_list[1]),int(date1_list[0]));
    date2_time=dt.date.today();
    days_num=abs(date1_time-date2_time);
    print days_num.days;
date_birth = raw_input("Enter Your birthday:DD/MM/YY:>");
total_days(date_birth);

def next_birthday(birthday):
    date1_list = birthday.split('/');
    date2_time = dt.date.today();
    next_year=dt.date.today().year+1;
    date1_time = dt.date(int(next_year), int(date1_list[1]), int(date1_list[0]));
    days_num = abs(date1_time - date2_time);
    print days_num.days;
next_birthday(date_birth);

