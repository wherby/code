
# https://leetcode.cn/contest/biweekly-contest-82/problems/minimum-sum-of-squared-difference/

def arrayChangeWithK(ls,k):
    n = len(ls)
    ls.sort()
    ls = [0]+ ls
    pls =[0]*(n+1)
    sm = sum(ls)
    for i in range(n+1):
        pls[i] = pls[i-1] + ls[i]
    acc =0
    for i in range(n,-1,-1):
        if acc >=k:
            break
        acc += (ls[i] - ls[i-1])*(n-i+1)
    ret = ls[1:i+1]
    remains =sm-k - pls[i]
    if remains <=0:
        remains =0
    for j in range(i+1,n+1):
        k = n -j +1
        ret.append(remains//k)
        remains -= remains//k
    return ret

ls = [1,3,7,8,9]
print(arrayChangeWithK(ls,0))
print(arrayChangeWithK(ls,4))
print(arrayChangeWithK(ls,26))
print(arrayChangeWithK(ls,23))
print(arrayChangeWithK(ls,28))
print(arrayChangeWithK(ls,27))
print(arrayChangeWithK(ls,49))