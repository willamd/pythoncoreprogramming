fobj=open('read_file.py','r');
data= fobj.readlines();
for index in range(0,len(data)):
    if data[index][0]!='#':
        print data[index],;
    else:
        continue;
