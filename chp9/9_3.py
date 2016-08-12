file_name=raw_input("Enter the filename:>");
fobj=open(file_name,'r');
data=fobj.readlines();
print len(data);
fobj.close();