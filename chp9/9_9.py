import sys,os
path="/usr/lib/python2.7";
file_list=os.listdir(path);
List_e=[];
List_f=[];
i=0;
for file in file_list:
    if os.path.splitext(file)[1]=='.py':
    # print os.path.splitext(file)[1]/[0][1] is the extension
        mapath=os.path.join(path,file);#output the path

        filename=open(mapath,'r');
        sign='__doc__';
        for eachline in filename:
            if eachline.find(sign)!=-1:
                List_f.append(os.path.basename(mapath));
                break;
        if i==len(List_f):
            List_e.append(os.path.basename(mapath));
        i=len(List_f);
print List_e;
print List_f;


