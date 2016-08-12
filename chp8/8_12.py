start=int(raw_input("Enter the start number:"));
end=int(raw_input("Enter the end number:"));
title= "DEC\tBIN\t\tOCT\tHEX";
if 126>=start>=32 or 126>=end>=32:
    title+="\tASCII";
else:
    pass
print title;
for i in range(start,end+1):
    if 126>=i>=32:
        print "%d\t%s\t%o\t%x\t%s"%(i,bin(i)[2:],i,i,chr(i));
    else:
        print "%d\t%s\t%o\t%x" % (i, bin(i)[2:], i, i);
