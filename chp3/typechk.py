#!/usr/bin/python
"""typechk.py--inspect the type of data type."""

import types

def displayNumType(num):
    print num, "is",
    if isinstance(num, (int, long, float, complex)):
        print "a number of type", type(num).__name__;
    else:
        print "not a number at all.";


displayNumType(-69);
displayNumType(9999999999);
displayNumType(98.6);
displayNumType(-5.2 - 1j);
displayNumType('xxx');

def display_num_type(num):
    print num, "is",
    if type(num)==types.IntType:  #type(0):
        print "an interger";
    elif type(num)==types.LongType:  #type(0L):
        print "an long";
    elif type(num)==types.ComplexType:  #type(0+0j):
        print "an complex";
    elif type(num)==types.FloatType:  #type(0.0):
        print "an float";
    else:
        print "not a number at all"
display_num_type(10);
display_num_type(10.0);

a=10;
print a;
del a;
#print a;
a=11;
print a;
