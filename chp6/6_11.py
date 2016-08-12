#!/usr/bin/python
#
#Time:2016-07-10
#Author:William
#Exercixe:6.11;IP convertion
ip=int(raw_input("Enter a number:>"));
part0=part1=part2=part3=0;
part3=ip%256;
part2=((ip-part3)/256)%256;
part1=(ip-part3-part2*256)/pow(256,2)%256;
part0=(ip-part3-part2*256-part1*256**2)/pow(256,3);
if part3>255:
    part3=255;
elif part2>255:
    part2=255;
elif part1>255:
    part1=255;
elif part0>=255:
    part0=255;
print "IP:%d.%d.%d.%d"%(part0,part1,part2,part3);

def convert_to_number(str1):
    list=str1.split('.');
    length=len(list)-1;
    result=0;
    for i in list:
        if i >=0 and i<256:
            result+=int(i)*pow(256,length);
            length-=1;
        else:
            print "Error"
    print result;
list=raw_input("Input the Ip address(xx.xxx.xxx.xx):>");
convert_to_number(list);