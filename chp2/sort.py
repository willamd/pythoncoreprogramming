#!/usr/bin/python
large = 0
small = 0
midle = 0
input1 = int(raw_input("Enter a number:"))
input2 = int(raw_input("Enter a number1:"))
input3 = int(raw_input("Enter a number2:"))

if input1 < input2:
    if input2 < input3:
        small = input1
        midle = input2
        large = input3
    elif input2 >= input3:
        if input1 < input3:
            small = input1
            midle = input3
            large = input2
print small, midle, large
