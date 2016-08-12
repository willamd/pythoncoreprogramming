# 1,1,2,3,5,8,13,21
def fbnqs(number):
    xs_list=[];
    xs_list.append(1);
    xs_list.append(1);
    if number>2:
        for i in range(2,number):
            xs_list.append(xs_list[i-1]+xs_list[i-2]);
    else:
        pass;
    print xs_list[number-1];
input_number=int(raw_input("input a number->"));
fbnqs(input_number);
