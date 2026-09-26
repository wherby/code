# https://leetcode.cn/problems/kth-smallest-amount-with-single-denomination-combination/?envType=daily-question&envId=2026-08-21
# 这里使用二进制反演，这里不用考虑coins是否互质？
# 在python里因为除法特性，不能使用负数作为除数求包含的个数,所以需要把数字和符号分别存储
from typing import List, Tuple, Optional
import math 
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        coins.sort()
        ls = []
        for i in range(1,1<<n):
            acc = 1
            sig = -1
            for j in range(n):
                if (1<<j)&i:
                    acc = math.lcm(acc,coins[j])
                    sig = sig*(-1)
            ls.append((sig,acc))
        #print(ls)
        def verify(md):
            sm =0 
            for sig,a in ls:
                sm += md //a *sig
            return sm >=k
        l = 0
        r= 10**30
        while l<r:
            md = (l+r)>>1
            if verify(md):
                r= md 
            else:
                l= md +1
        return l

print(14//-5)
