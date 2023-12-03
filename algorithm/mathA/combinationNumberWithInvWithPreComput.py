# https://github.com/wisdompeak/LeetCode/blob/master/Template/Combination-Number/comb.cpp
# this will time out in  https://leetcode.cn/contest/weekly-contest-374/problems/count-the-number-of-infection-sequences/submissions/
# will pass with pre-compute in comb2 function 
# with comb2(n,m) = f(n) * inv(n-m) *inv(m)  

mod = 10**9+7
N = 10**5
def quickPow(x,y):
    ret =1
    cur = x 
    while y >0:
        if y & 1:
            ret = ret * cur % mod
        cur = cur *cur % mod
        y = y //2
    return ret


prels = [1]*(N+1)

def getInvArray(n,mod = 10**9+7):
    inv = [1]*(n+1)
    acc = 1
    for i in range(1,n+1):
        acc =acc*i%mod
        prels[i] = acc
    inv[-1] = quickPow(acc,mod-2)
    for i in range(n-1,-1,-1):
        inv[i] = inv[i+1]*(i+1) %mod
    return inv

def inv(x):
    return quickPow(x,mod-2)
invls = getInvArray(10**5)
def comb2(n,m, mod= 10**9+7):
    cnt = prels[n]* invls[n-m] * invls[m] %mod
    return cnt

print(comb2(10000,200))
import math # use default lib
print(math.comb(10000,200)%mod)