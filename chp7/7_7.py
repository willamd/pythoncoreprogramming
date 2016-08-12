#coding=utf-8
#
#Time:2016-07-18
#Author:William
#
#7_7
#
####################

dict_d={1: 'abc', 2: 'def', 3: 'ghi', 4: 'jkl', 5: 'mno'};
dict_r={};
for i in dict_d.keys():
    dict_r[dict_d[i]]=i;
print dict_r;
