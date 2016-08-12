a=[1,2,3,4,5];
b=['abc','def','ghi','jkl','mno'];
length=len(a);
dic_t={};
if len(a)!=len(b):
    print("Error!");
else:
    for i in range(length):
        dic_t[a[i]]=b[i];
print (dic_t);

dict_d=dict(zip(a,b));
print dict_d

