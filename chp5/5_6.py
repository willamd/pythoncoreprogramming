#!/usr/bin/python
#
#Time:2016-07-08
#Author:William
#Exercixe:5.6

def digit(num):
    if str(num).isdigit():
        return True;
    else:
        return False;

def calculator():
    print "Input the expression.Such as 1+2:";
    expression = raw_input("The expression is:")
    if len(expression.split('+'))==2:
        value1=expression.split('+')[0];
        value2=expression.split('+')[1];
        if digit(value1) and digit(value2):
            return eval(value1)+eval(value2);
    elif len(expression.split('-'))==2:
        value1 = expression.split('-')[0];
        value2 = expression.split('-')[1];
        if digit(value1) and digit(value2):
            return eval(value1)-eval(value2);
    elif len(expression.split('*'))==2:
        value1 = expression.split('*')[0];
        value2 = expression.split('*')[1];
        if digit(value1) and digit(value2):
            return eval(value2)*eval(value1);
    elif len(expression.split('/'))==2:
        value1 = expression.split('/')[0];
        value2 = expression.split('/')[1];

        if value2==0:
            print "error.";
            return 0;
        else:
            if digit(value1) and digit(value2):
                return eval(value1)/eval(value2);
    elif len(expression.split('**'))==2:
        value1 = expression.split('**')[0];
        value2 = expression.split('**')[1];
        if digit(value1) and digit(value2):
            return eval(value1)**eval(value2);
print calculator();


