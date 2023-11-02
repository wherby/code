# https://github.com/wisdompeak/LeetCode/blob/master/Template/Combination-Number/comb.cpp

mod = 10**9 +7
def quickPow(x,y):
    ret =1
    cur = x 
    while y >0:
        if y & 1:
            ret = ret * cur % mod
        cur = cur *cur % mod
        y = y //2
    return ret

def inv(x):
    return quickPow(x,mod-2)
def comb2(n,m, mod= 10**9+7):
    cnt = 1
    acc =1
    for i in range(m):
        cnt *=(n-i) %mod
        acc *= (i+1)%mod
    cnt = cnt* inv(acc)%mod
    return cnt

print(comb2(10000,200))
import math # use default lib
print(math.comb(10000,200)%mod)