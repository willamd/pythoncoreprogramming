def copy(file1,file2):
    fobj1=open(file1,'r');
    fobj2=open(file2,'w');
    for line in fobj1:
        fobj2.write(line);
    fobj1.close();
    fobj2.close();
file1=raw_input("File1:>");
file2=raw_input("File2:>");
copy(file1,file2);
