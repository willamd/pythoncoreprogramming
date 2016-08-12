#!/usr/bin/env python
test=[1,2,3,4,5];
result=0;
for i in test:
	result+=i;
print result;
test=0;
for i in range(5):
	test+=int(raw_input("Enter a number:"));
print test;
i=0;
while_result=0;
while i<5:
	while_result+=int(raw_input("Enter a number1:"));
	i+=1;
print while_result;
print sum(int(raw_input("Enter a number2:")) for j in range(5));

