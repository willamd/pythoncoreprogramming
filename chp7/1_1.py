#!/usr/bin/python
#coding=utf-8
#
#Time:2016-07-14
#Author:William
#
#usrpw.py
#
####################

db={};
def newuser():
    promote="login desired:";
    while True:
        name=raw_input(promote);
        if db.has_key(name):
            promote='name taken,try another:';
            continue;
        else:
            break;
    pwd=raw_input('Passwd:');
    db[name]=pwd;

def olderuser():
    name=raw_input("Login:");
    pwd=raw_input("passwd:");
    passwd=db.get(name);
    if pwd==passwd:
        print "Welcome back,",name;
    else:
        print "login incorrect";
def showmenue():
    promote="""
    (N)ew User login
    (E)xisting User Login
    (Q)uit
    Enter your choice:"""
    done=False;
    while not done:
        choose=False;
        while not choose:
            try:
                choice=raw_input(promote).strip()[0].lower();
            except (EOFError,KeyboardInterrupt):
                choice='q';
            print "\nYou picked[%s]"%choice;
            if choice not in 'neq':
                print "invalid option,try again."
            else:
                choose=True;
        if choice=='q':
            done =True;
        if choice=='n':
            newuser();
        if choice =='e':
            olderuser();


if __name__=='__main__':
    showmenue();
