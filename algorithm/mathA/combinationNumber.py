# https://github.com/wisdompeak/LeetCode/blob/master/Template/Combination-Number/comb.cpp

comb = [[0]*1001 for i in range(1001)]
for i in range(1001):
    comb[i][i] , comb[i][0]=1,1
    if i == 0: continue
    for j in range(1,i):
        comb[i][j] = comb[i-1][j-1] + comb[i-1][j]

print(comb[100][:10])

def comb2(n,m):
    cnt = 1
    for i in range(m):
        cnt *=n-i
        cnt //= i+1
    return cnt

print(comb2(100,2))

## Using Lib
import math
print(math.comb(100,2))
print(comb2(1234,23) == math.comb(1234,23))

# combination number
#>>> from math import comb
#>>> comb(10,3)
#120
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

print(comb2(100000,20000))
import math # use default lib
print(math.comb(10000,200)%mod)