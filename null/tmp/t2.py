def reduce(s):
    if len(s)<3:
        return s
    res =""
    res+= s[0]
    for i in range(1,len(s)-1):
        if s[i-1]=="0" and s[i+1]=="0":
            continue
        else:
            res= res +s[i]
    res= res +s[-1]
    return res

a= "000000000101"*10000
cnt =0 
while a!= reduce(a):
    cnt +=1
    a = reduce(a)

print(cnt)