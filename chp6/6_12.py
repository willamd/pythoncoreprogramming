#!/usr/bin/python
#
#Time:2016-07-10
#Author:William
#Exercixe:6.12.
def fchar(string,char):
    list=[];
    for i,j in enumerate(string):
        #print i,j;
        if j==char:
            list.append(i);
    if len(list)==0:
        return -1;
    else:
        return list;
list=raw_input("Enter a string:>");
list_char=raw_input("Enter the char to be found:>")
print fchar(list,list_char);
def rfindchar(string,char):
    list=[];
    for i,j in enumerate(string):
        #print i,j;
        if j==char:
            list.append(i);
    if len(list)==0:
        return -1;
    else:
        return list[len(list)-1];
print rfindchar(list,list_char);

def subchr(string,origchar,newchar):
    result='';
    for i in string:
        # print i,j;
        if i == origchar:
            result+=newchar;
        else:
            result+=i;
    return result;


print subchr(list, list_char,'c');
