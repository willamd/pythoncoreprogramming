#coding=utf-8
#!/usr/bin/python
#
#Time:2016-07-11
#Author:William
#Exercixe:6.14
import random as rd
def Rochambeau(choice_str):
    choice={'1':"bu",'2':"st","3":"jd"};
    result={"12":"win",'21':"lose","13":"lose","32":"lose","31":"win","23":"win","11":"ps","22":"ps","33":"ps"};
    rdindex=str(rd.randint(1,3));
    print "The computers choice is :%s"%(choice[rdindex]);
    print "Your choice is ",choice[choice_str];
    com_result=choice_str+rdindex;
    print com_result;
    if result[com_result]=="win" or result[com_result]=="ps":
        print result[com_result];
    else:
        print "You lose."
choice=raw_input("Choice->\n(1):bu \n(2):st,\n(3):jd\nEnter your choice:");
Rochambeau(choice);

