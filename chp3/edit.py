#!/usr/bin/python
"""The file is used to edit file"""
import os

ls=os.linesep;
all_content=[];
line_numer=0;

while True:
    fname=raw_input("Enter the file name:>");
    if os.path.exists(fname):
        fobj=open(fname,'r+');
        for line in fobj:
            all_content.append(line);
            line_numer+=1;
        fobj.close();
        print all_content;
        break;
    else:
        print "Error,%s file does not exsits.\n"%fname;
        break;
print "Input '.' to quit!"
while True:
    edit_number=int(raw_input("Enter the edit number[1,%d]"%line_numer));
    if edit_number <= line_numer and edit_number >= 1:
        print all_content[edit_number];
        new_content=raw_input("Input the new content>");
        if new_content!='.':
            all_content[edit_number-1]=new_content;
    else:
        print "Error,The edit number is illegle.";
        break;
fobj=open(fname,'w');
fobj.writelines(['%s%s'%(x,ls) for x in all_content]);
fobj.close();
