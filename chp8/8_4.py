#!/usr/bin/python
#coding=utf-8
#
#Time:2016-08-02
#Author:William
#
#8_4
#
####################
def isprime(number):
    begin=1;
    end=number;
    result=0;
    while begin<=end:
        if number%begin==0:
            result= begin;
            begin+=1;
        else:
            begin+=1;
            continue;
    return result;
def sushu(number):
    begin=2;
    end=number-1;
    Flag=True;
    count=0;
    while begin<=end:
        if number%begin==0:
            begin+=1;
            count+=1;
        else:
            if count >=2:
                Flag=False;
                break;
            else:
                Flag=True;
                begin+=1;
    return Flag;
def getfactors(numb):
    begin=1;
    end=numb;
    while begin<=end:
        if numb%begin==0:
            print begin,;
            begin+=1;
        else:
            begin+=1;
def shlist(number):
    begin = 2;
    tmp=number;
    print '*'
    if sushu(tmp):
        print tmp,;
    else:
        while begin <= tmp:
            if number % begin != 0:
                begin += 1;
            else:
                tmp=tmp/begin;
                if tmp!=1:
                    if sushu(begin):
                        print begin,;
                        return shlist(tmp);
                else:

                    break;

test=int(raw_input("Input a number:"));
print isprime(test);
print sushu(test);
getfactors(test);
print
shlist(test);
##isprime and getfactors
