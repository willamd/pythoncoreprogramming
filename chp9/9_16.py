def adapter(str_input):
    result=[];
    str_len=len(str_input.split());
    total_len=len(str_input);
    print total_len;
    if total_len <=10:
        result.append(str_input);
    else:
        for i in range(str_len-1,-1,-1):
            print i;
            part_len=len(str_input.split()[i]);
            print part_len;
            total_len -=part_len+1;
            print total_len;
            if total_len<=9:
                result.append(str_input[:total_len]);
                result.append((str_input[total_len:]));
                break;
            else:
                continue;
    print result;
input_s=raw_input("tet");
adapter(input_s);

