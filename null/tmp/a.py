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
#print(a)


d = 3
arr1 = [[0]*d for _ in range(d)]
for i in range(d):
    for j in range(i+1,d):
        arr1[i][j] = 1 
print(arr1)
arr2 = [[0]*d for _ in range(d)]
for i in range(d):
    for j in range(i):
        arr2[i][j] = 1 
print(arr2)

arr3 = [[0]*2*d for _ in range(2*d)]
for i in range(d):
    for j in range(i):
        arr3[i][d+j] = 1
    for j in range(i+1,d):
        arr3[d+i][j] =1
print(arr3)
arr4 = [[0]*d for _ in range(d)]
for i in range(d):
    for j in range(d-1-i):
        arr4[i][j] = 1 
print(arr4)