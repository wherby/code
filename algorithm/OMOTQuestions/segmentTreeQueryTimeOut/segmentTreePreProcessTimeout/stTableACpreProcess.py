# https://leetcode.cn/problems/minimum-stability-factor-of-array/submissions/641704624/

from typing import List, Tuple, Optional
import math
from functools import cache

@cache
def gcd1(a,b):
    return math.gcd(a,b)

class SparseTable:
    __slots__ = 'op', 'st'
    def __init__(self, nums, op):
        # op 需要满足可重复贡献，即 x op x = x，如 max, min, gcd, lcm, and, or
        # 建立 O(nlogn)，查询 O(1)
        n = len(nums)
        m = n.bit_length()
        st = [[0] * (n - (1<<b) + 1) for b in range(m)]
        for i, x in enumerate(nums):
            st[0][i] = x
        for b in range(1, m):
            l = 1 << (b-1)
            for i in range(n - (1<<b) + 1):
                st[b][i] = op(st[b-1][i], st[b-1][i+l])
        self.op = op
        self.st = st

    def query(self, left, right):
        b = (right - left + 1).bit_length() - 1
        return self.op(self.st[b][left], self.st[b][right - (1<<b) + 1])

class Solution:
    def minStable(self, nums: List[int], maxC: int) -> int:
        t1 =len([a for a in nums if a != 1])
        if t1 -maxC <=0:
            return 0
        n = len(nums)

        st = SparseTable(nums,gcd1)

        lfrom = 0
        dic ={}
        #Using two pointer and SpareTree
        for i in range(n):
            while st.query(lfrom,i) ==1 and lfrom < i:
                lfrom +=1
            dic[i] = lfrom

        #print(dic)
        def verify(md,c):
            lst = -1
            for i in range(n):
                if min(i- dic[i] +1,i-lst) > md:
                    if c:
                        c -=1
                        lst =i
                    else:
                        return False
            return True
        l ,r  = 1, n+1
        r = n //(maxC+1)
        while l < r:
            md = (l+r)>>1
            #rint(md,verify(md,maxC))
            if verify(md,maxC):
                r = md 
            else:
                l = md +1
        return l

from v5input import nums,maxC
re = Solution().minStable(nums,maxC)
print(re)