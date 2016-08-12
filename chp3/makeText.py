#!/usr/bin/python

"""makeText.py --create text file"""

import os

ls = os.linesep;  # \n

# Get the file
while True:

    fname = raw_input("Enter a file name->");
    if os.path.exists(fname):
        print "Error:'%s' already exists" % fname;
    else:
        break;

# Get  file content
all = [];

print "\nEnter lines('.' by itself to quit).\n"

while True:
    entry = raw_input('>');
    if entry == '.':
        break;
    else:
        all.append(entry);

# Write lines to file with proper line-ending
fobj = open(fname, 'w');
fobj.writelines(['%s%s' % (x, ls) for x in all]);
fobj.close();
print "DOne.\n";
