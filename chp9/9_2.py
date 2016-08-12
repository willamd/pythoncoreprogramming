import os
lines=int(raw_input("Enter the number of lines you want to read(NO.)"));
filename=raw_input("Enter the file name you want to read(Name).");
fobj=open(filename,'r');
data=fobj.readlines();
if len(data)>lines:
    for i in range(lines):
        print data[i],;
else:
    for i in range(len(data)):
        print data[i],;
