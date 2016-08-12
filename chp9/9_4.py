file_name=raw_input("Enter the filename:>");
line_no=int(raw_input("Enter the line to read one time:"));
fobj=open(file_name,'r');
data=fobj.readlines();
file_length= len(data);
start=0;
end=0;
if file_length >= line_no:
    end=line_no;
else:
    end=file_length;
anykey=raw_input("Press enter\n");
while anykey!=' ':
    if end<=file_length:
        for i in range(start, end):
            print data[i],;
    else:
        for i in range(start, file_length):
            print data[i],;
        break;
    start+=line_no;
    end+=line_no;
    anykey = raw_input("Press any key continue");
fobj.close();


