import os
fobj = open('9_1.py')
count = 0
for eachline in fobj:
    print eachline,
    count += 1
    if count%2 == 0:
        os.system('read -s -n 1 -p "Press any key to continue"');
    print
    continue
fobj.close()