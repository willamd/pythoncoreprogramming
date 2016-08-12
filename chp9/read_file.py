'''file=open('../test.txt','rw');
# data=[lines.strip() for lines in file.readlines()]
# file.seek(2);
# print data;
for i in range(5):
    print file.next();

# data_seek=[line.strip() for line in file.seek(0)];
# print data_seek;
file.close();'''
import os
filename=raw_input("Enter a file to read>");
fobj=open(filename,'a');
print os.stat('../test.txt');
print fobj.fileno();
while True:
    aline=raw_input("Enter '.' to quit.");
    if aline !='.':
        fobj.write("%s%s"%(aline,os.linesep));
        print fobj.tell();
    else:
        break;
fobj.close();