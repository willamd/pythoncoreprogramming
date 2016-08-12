#!/usr/bin/python
#
#Time:2016-07-08
#Author:William
#Exercixe:5.5

def change(num):
    if num>=25:
        temp = divmod(num,25);
        print "25-%d"%temp[0];
        return change(temp[1]);
        #exit(0);
    elif num >= 10 and num<25:
        temp = divmod(num,10);
        print "10-%d"%temp[0];
        return change(temp[1]);
    elif num>= 5 and num<10:
        temp = divmod(num,5);
        print "5-%d" % temp[0];
        return change(temp[1]);
    elif num >= 1 and num < 5:
        temp = divmod(num,5);
        print "1-%d" % temp[1];
        return 0
    else:
        return 0;
        #exit(0);

change(100);
change(77);



