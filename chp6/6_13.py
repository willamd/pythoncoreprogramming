#coding=utf-8
#!/usr/bin/python
#
#Time:2016-07-10
#Author:William
#Exercixe:6.13
def atoc(string):
    #采用中问注释,rfind('s')返回s字符最后出现的位置
    index=string.rfind('-');#如果有-符号的话;
    if index<=0:
        index=string.rfind('+');#找出+号的位置
    if index>=0:
        real=float(string[0:index]);
        imag=float(string[index+1:-1]);
        print imag;
    return complex(real,imag)

print atoc('1.23e+3-5.67j')
