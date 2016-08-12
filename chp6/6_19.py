#coding=utf-8
#!/usr/bin/python
#
#Time:2016-07-11
#Author:William
#Exercixe:6.19

print "Input the matrix 1,2,3,4 as a row and input Q to quit the input";
list=[];

while True:
    row_list=raw_input("Enter a row NO.->");
    if row_list!="Q":
        data_list=row_list.split(',');
        for i in data_list:
            list.append(int(i));
    elif row_list=="Q":
        break;
    else:
        break;
print "Choose which style you want to display the data\n(1):vertical\n(2):Herical"
V_H=raw_input("Enter the choice:(1) or (2)");
elements=raw_input("Enter the elements you want to display ervery row/column");

def display(list,V_H,elements):
    elements=int(elements);
    num=len(list)/elements;
    if int(V_H)==2 and (len(list)-num*elements)==0:
        for i in range(num):
            for j in range(elements):
                print list[i*num+j],;
            print ;
    if int(V_H) == 2 and (len(list) - num * elements) > 0:
        for i in range(num):
            for j in range(elements):
                print list[i*num+j],
            print ;
        for k in list[(num) * elements:]:
            print k,
display(list,V_H,elements);

