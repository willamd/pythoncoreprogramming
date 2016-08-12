import os

for tempdir in('read_file.py',r'c:\temp'):
    if os.path.isdir(tempdir):
        break;
    else:
        print "no temp dir avaliable.";
        tempdir='';
    if tempdir:
        os.chdir(tempdir);
        cwd=os.getcwd();
        print "Current dir is%s"%cwd;
        os.mkdir('test');
        os.chdir('test');
        cwd=os.getcwd();
        print "The current dir is %s"%cwd;
        print os.listdir();