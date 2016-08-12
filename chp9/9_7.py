file=open('/etc/group','r');
option={}
for line in file:
    index=line.find(':');
    if index!=-1:
        key=line[1:index];
        value=line[index+1:];
        option[key]=value;
    if key in option:
        print key,"=",option[key];
file.close();

