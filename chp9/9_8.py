moudle_name=raw_input("moudle name:>");
obj=__import__(moudle_name);
att_list=dir(obj);
for item in att_list:
    print 'name:',item;
    print "type:",type(item);
    print "value:",getattr(obj,item);
