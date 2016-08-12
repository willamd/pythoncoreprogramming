#!/usr/bin/python
#
#Time:2016-07-10
#Author:William
#Exercixe:6.5
def befor_after():
    a = raw_input("Please input a string ... ")
    print 'Display in for loop:'
    for i in a:
        print i,
    print '\nDisplay in while loop:'
    j = 0
    while (j < len(a)):
        if j!=len(a)-1:
            if j>=1:
                print a[j-1]+a[j]+a[j+1];
            else:
                print a[j]+a[j+1];
        else:
            print a[j-1]+a[j];
        j = j + 1;
befor_after();
def str_comp(str1,str2):
    index=0;
    if len(str2)!=len(str1):
        print 'not';
    else:
        for i in str1:
        #print index;
            if index<len(str2):
                if i == str2[index]:
            #print index;
                    index+=1;
                else:
                    print "not";
                    break;
            else:
                print "not";
                break;
str_comp('dlc','al')

def huiwen(str1):
    length=len(str1)-1;
    index=0;
    while str1[index]==str1[length]:
        #print index,length;
        if (index+1)!=length or index!=length:
            index+=1;
            length-=1;
        else:
            print "not huiwen";
            break;

huiwen("dlcclad");

def reverse(str1):
    length=len(str1)-1;
    result='';
    while length>=0:
        result+=str1[length];
        length-=1;
    return str1+result;
print reverse('dlc');
