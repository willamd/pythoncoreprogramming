total_names=raw_input("Enter total numbers of name:");
list_name=[];
err=0;
if total_names.isdigit():
    for i in range(int(total_names)):
        name=raw_input("Please enter name %d :"%i);
        if ',' not in name:
            err+=1;
            print "Wrong format.....should be Last,First";
            print "You have done this %d time(s) already.Fixing input"%err;
        else:
            list_name.append(name);
else:
    print "The input type is error!";
list_name.sort();
print list_name;



