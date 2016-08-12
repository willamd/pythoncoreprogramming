def cal(str_ex):
    expression=str_ex.split();
    if expression[1] not in ("+-*/%"):
        print "the format is wrong";
    else:
        if expression[1]=='+':
            print eval(expression[0])+eval(expression[2]);
        elif expression[1]=='-':
            print eval(expression[0])-eval(expression[2]);
        elif expression[1] == '*':
            print eval(expression[0]) * eval(expression[2]);
        elif expression[1] == '-':
            print eval(expression[0]) / eval(expression[2]);
        elif expression[1] == '%':
            print eval(expression[0]) % eval(expression[2]);
        else:
            print "Does not surrport";
expression=raw_input("Enter the expression:>");
cal(expression);
