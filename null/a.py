def f1(str1):
    res =set([])
    for i in range(1,len(str1)-1):
        if str1[i-1] == str1[i+1] =="0":
            res.add(i)
    ret =""
    for i in range(len(str1)):
        if i not in res:
            ret= ret +str1[i]
    return ret 

a = "10101001000001"
a =a *10000
while a != f1(a):
    a = f1(a)
print(a)