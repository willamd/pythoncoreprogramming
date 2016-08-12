#!/usr/bin/python
#coding=utf-8
#
#Time:2016-08-02
#Author:William
#
#8_0
#
####################

print [(x+1,y+1) for x in range(3) for y in range(5)];
import os
#print os.stat('test.txt').st_size;
f=open('test.txt','r');


#print len([word for line in f for word in line.split()]);
#print sum(len(word) for line in f for word in line.split());
#[expr for iter_var in iteration if condition]
for lines in f:
    print lines;
    #print lines.split();
    for word in lines.split():
        print word;
f.close();
f=open('test.txt','r');
longest=0;
while True:
    length=len(f.readline().strip());
    if not length:break;
    if length>longest:
        longest=length;
f.close();
print '*'*8
print longest;