#!/usr/bin/python
#coding=utf-8
#
#Time:2016-07-14
#Author:William
#
#7_3
#
####################

test=dict(x=1,y=6,z=4,u=5);
print sorted(test.keys());
sort_dict=sorted(test.keys());
for i in sort_dict:
    print i,test.get(i);
value_sorted=sorted(test.values());
print value_sorted;
for i in value_sorted:
    for j in test.keys():
        if i==test[j]:
            print j,':',i;
        else:
            continue;