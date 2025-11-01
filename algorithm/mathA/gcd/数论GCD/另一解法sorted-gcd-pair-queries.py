# https://leetcode.cn/problems/sorted-gcd-pair-queries/submissions/673638384/
# 
from typing import List, Tuple, Optional

from collections import Counter
def prepare(M):
    # 初始化数组
    mu = [1] * M  # 莫比乌斯函数
    F = [0] * M   # 最小质因子
    q = []        # 存储质数
    
    mu[1] = 1     # 规定mu[1] = 1
    
    for i in range(2, M):
        if not F[i]:  # i是质数
            F[i] = i
            q.append(i)
            mu[i] = -1  # 质数的mu值为-1
        
        # 用当前已筛出的质数q[j]去标记合数i*q[j]
        for p in q:
            if i * p >= M:
                break
            F[i * p] = p  # 合数i*p的最小质因子是p
            if i % p == 0:
                mu[i * p] = 0  # i*p包含平方因子p^2
                break
            else:
                mu[i * p] = -mu[i]  # 根据mu的定义更新
    
    return mu, F, q

import math
def getMlengthGcd(ls,m):
    c = Counter(ls)
    mx = max(ls)
    mu, F, primes = prepare(mx+1)
    gcd_count = [0]*(mx+1)
    for i in range(1,mx+1):
        for j in range(i*2,mx+1,i):
            c[i] += c[j]

    for i in range(1,mx+1):
        for j in range(1,mx//i +1):
            gcd_count[i] += mu[j]*math.comb(c[j*i],m)
    return gcd_count

from bisect import bisect_right,insort_left,bisect_left
class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        gcdcnt = getMlengthGcd(nums,2)

        ls = []
        acc = 0
        for i,a in enumerate(gcdcnt):
            acc += a 
            ls.append(acc)
        ans = []
        #print(ls)
        for q in queries:
            ans.append(bisect_left(ls,q+1))
        return ans

ls = [2,3,4,6,8,12]
re =Solution().gcdValues(nums = [2,3,4], queries = [0,2,2])
print(re)
