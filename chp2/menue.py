#!/usr/bin/python
print"(1)Sum of five number\n(2)Average of five number\n(X)Exit."
choose=raw_input("Choose you option:");
resutl=0;
if choose=='1':
	test=[1,2,3,4,5];
	print test;
	print sum( i for i in test);
elif choose=='2':
	test=[1,2,3,4,5];
	print test;
	print sum(i for i in test)/len(test);
elif choose=="X":
	exit();
else:
	print "wrong input\n";