import os
file=open('../test.txt','rw');
longest=0;
while True:
    linelen=len(file.readline().strip());
    if longest<linelen:
        longest=linelen;
    if not linelen:
        break;

print longest;
file.close();
file=open('../test.txt','rw');
print file.readlines();
file.close();

