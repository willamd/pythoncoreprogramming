import zipfile;
def add(filename,zipf):
    zipopen=zipfile.ZipFile(zipf,'a');
    zipopen.write(filename);
    zipopen.close();
def create(zipf,file_content):
    zipp=zipfile.ZipFile(zipf,'w');
    zipp.write(file_content);
    zipp.close();
def extractt(zipf,filename):
    zipf=zipfile.ZipFile(zipf,'r');
    zipf.extract(filename);
    zipf.close();

# create('test.zip','test.txt');
# add('test.gz','test.zip')
extractt('test.zip','test.gz')

