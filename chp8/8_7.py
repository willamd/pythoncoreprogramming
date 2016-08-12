def isperfect(number):
    begin=1;
    end=number-1;
    result=0;
    while begin<=end:
        if number%begin==0:
            print begin
            result+=begin;
            begin+=1;
        else:
            begin+=1;
    if result == end:
        return 1;
    else:
        return 0;
def factorial(number):
    if number==1:
        return 1;
    else:
        return number*factorial(number-1);
test=int(raw_input("Input a number:"));
isperfect(test);
print factorial(test);

