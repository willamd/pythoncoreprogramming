#!/usr/bin/env python
a=0;
while a <= 10:
	print a;
	a+=1;
for b in range(11):
	print b;
in_put=int(raw_input("Enter a number:"));
if in_put>0:
	print "This is a active number;"
elif in_put<0:
	print "This is a negtive number;"
else:
	print "This number is %d"%in_put;

#While and for loop to output str

str_dlc="This is a test";
a=0;
while a <len(str_dlc):
	print str_dlc[a];
	a+=1;
for i,ch in enumerate(str_dlc):
	print ch;
