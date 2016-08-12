def compstr(str1,str2):
    result=-1;
    # print str1;
    # print str2;
    if len(str1)==len(str2):
        if str1==str2:
            result=-1;
        else:
            for index in range(0,len(str1)):
                if str1[index]==str2[index]:
                    continue;
                else:
                    # print index;
                    result= index;
                    break;
    else:
        if len(str1)<len(str2):
            for index in range(0,len(str1)):
                if str1[index]==str2[index]:
                    continue;
                else:
                    result=index;
                    break;
        else:
            for index in range(0,len(str2)):
                if str1[index]==str2[index]:
                    continue;
                else:
                    result=index;
                    break;
    return result;
file1=raw_input("Enter the file name 1:>");
file2=raw_input("Enter the file name 2:>");
fobj1=open(file1,'r+');
fobj2=open(file2,'r+');
data1=fobj1.readlines();
data2=fobj2.readlines();
length=0;
if len(data1)>len(data2):
    length=len(data2);
else:
    length=len(data1);
# print data1;
# print data2;
for index in range(0,length):
    # print data1[index],;
    # print data2[index],;
    result=compstr(data1[index],data2[index]);
    # print result;
    if result!=-1:
        print "col:%d-column:%d"%(index+1,result+1);
        break;
    else:
        continue;
fobj1.close();
fobj2.close();

