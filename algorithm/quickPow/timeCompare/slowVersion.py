from typing import List, Tuple, Optional

import time


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

def multiply(mat1,mat2,mod =10**9+7):
    n = len(mat1)
    res = [[0]*n for _ in range(n)]
    for i in range(n):
            for j in range(n):
                for k in range(n):
                    res[i][j] += mat1[i][k] *mat2[k][j]
                    res[i][j] %= mod
    return res
class Solution:
    @clock
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod = 10**9+7
        m = r-l +1
        idp = [0]*2*m
        mxt = [[0]*(m*2) for _ in range(m*2)]
        for i in range(m):
            for j in range(m):
                if i>j:
                    mxt[i][j+m]  =1
                if i<j:
                    mxt[i+m][j] =1
        for i in range(m):
            idp[i] =i 
            idp[m+i] = m-1-i
        #print(mxt)
        mxt = quickPow(mxt,n-2)
        acc = 0
        for i in range(2*m):
            
            for j in range(2*m):
                acc += mxt[i][j]*idp[i]
                acc %=mod 
        return acc



re =Solution().zigZagArrays(10000000,1,75)
print(re)