from typing import List, Tuple, Optional

import time

mod = 10**9 + 7


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0 
        name = func.__name__
        arg_str = ", ".join(repr(arg) for arg in args)
        print('[{0}] {1}' .format( elapsed, name))
        return result
    return clocked


def quickPow(mat,k):
    n = len(mat)
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        res[i][i] =1 
    cur = [list(mat[i]) for i in range(n)]
    while k :
        if k %2 ==1:
            res = multiply(res,cur)
        k = k //2
        cur = multiply(cur,cur)
    return res

def multiply(a,b,mod =10**9+7):
    return [[sum(x * y for x, y in zip(row, col)) % mod for col in zip(*b)]
            for row in a]

def vecmul(v,mat,mod =10**9+7):
    n = len(v)
    w = [0]*n
    for i in range(n):
        vi = v[i]
        if vi:
            Ai = mat[i]
            for j in range(n):
                w[j] = (w[j] + vi * Ai[j]) % mod
    return w

class Solution:
    @clock
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod = 10**9+7
        m = r-l +1
        idp = [1]*m
        m1,m2 = [[0]*m for _ in range(m)] ,[[0]*m for _ in range(m)] 
        for i in range(m):
            for j in range(m):
                if i<j:
                    m1[i][j]  =1
                if i>j:
                    m2[i][j] =1

        mm = multiply(m1,m2)
        if (n-1)%2==0:
            M= quickPow(mm,(n-1)//2)
        else:
            M = multiply(m2,quickPow(mm,(n-2)//2))
        # idp = vecmul(idp,M)
        # return sum(idp)*2%mod
        #print(M,m1,m2)
        dp = [1] * m
        dp2 = [0] * m
        for i in range(m):
            for j in range(m):
                dp2[i] = (dp2[i] + M[i][j] * dp[j]) % mod
        return sum(dp2) * 2 % mod



#re =Solution().zigZagArrays(10000000,1,75)
re =Solution().zigZagArrays(3,1,3)
print(re)