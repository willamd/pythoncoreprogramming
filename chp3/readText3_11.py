#!/usr/bin/python

"""readText3_11.py--read and display text file."""
fname=raw_input("Enter a filename>");
print "The file name is %s"%fname;

try:
    fobj=open(fname,'r');
except IOError,e:
    print "***File con not open",e;
else:
    #display the data to the screen
    for eachline in fobj:
        print eachline.strip();#The ',' is used to not output \n
    fobj.close();
