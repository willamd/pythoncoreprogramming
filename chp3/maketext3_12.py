#!/usr/bin/python
"""This is a try except"""
import os
ls=os.linesep;
def maketext():
    while True:
        fname = raw_input("Enter a filename:>");
        try:
            open(fname, 'r');
            print "***Error %s is already exists"%fname;
        except IOError:
            break;
            fobj.close();
    #Get the file content
    all=[];#To store the input data
    print "\nEnter lines('.' by itself to quit).\n"
    while True:
        file_data=raw_input(">");
        if file_data=='.':
            break;
        else:
            all.append(file_data);
    fobj=open(fname,'w');
    fobj.writelines(['%s%s'%(x,ls) for x in all])
    fobj.close();
    print "Done\n"
def readtext():
    fname=raw_input("Enter the readed file name>");
    if os.path.exists(fname):
        fobj=open(fname,'r');
        for eachline in fobj:
            print eachline,;
    else:
        print"The file does not exists.\n";
print "(m)Make a new file.\n(r)read form a file."
option=raw_input("Enter your option->");
if option=="m":
    maketext();
elif option=='r':
    readtext();








