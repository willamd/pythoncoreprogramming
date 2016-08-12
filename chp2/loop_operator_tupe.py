#!/usr/bin/python
tupe = (1, 2, 3, 4, 5)
result = 0
for i in tupe:
    result += i
print result / len(tupe)
flag = True
while flag:
    input_r = int(raw_input())
    if input_r > 1 and input_r < 100:
        flag = False
        print"Suceess"
    else:
        print "Error"
        continue;
 continue;
