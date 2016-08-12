import gzip
# file1=open('test.t','rw');
# gz=gzip.open('test.gz','w');
# gz.writelines(file1);
# gz.close();
# file1.close();

f=gzip.open('test.gz','rw');
ff=open('test.txt','wb');
ff.writelines(f);
f.close();
ff.close();