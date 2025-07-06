# https://leetcode.cn/problems/minimum-stability-factor-of-array/submissions/641704624/

from typing import List, Tuple, Optional
import math
from functools import cache
from collections import defaultdict,deque


def logTrick(nums):
    n = len(nums)
    ret = [i for i in range(n)]
    acc =[]
    for i,a in enumerate(nums):
        # 计算以 i 为右端点的子数组 GCD
        for j,(b,idx) in enumerate(acc):
            acc[j][0] = math.gcd(b,a)
        # nums[i] 单独一个数作为子数组
        acc.append([a,i])
        idx = 1 
        for j in range(1,len(acc)):
            if acc[j][0] != acc[j-1][0]:
                acc[idx] = acc[j]
                idx +=1
        del acc[idx:]
        # while len(acc)>idx:
        #     acc.pop()
        # 去掉不满足的值
        while acc and acc[0][0] ==1:
            acc.pop(0)
        if len(acc):
            ret[i] = acc[0][1]
    return ret



class Solution:
    def minStable(self, nums: List[int], maxC: int) -> int:
        t1 =len([a for a in nums if a != 1])
        if t1 -maxC <=0:
            return 0
        n = len(nums)

        dic =logTrick(nums)
        #Using two pointer and SpareTree
        #print(dic)

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
#re = Solution().minStable(nums,maxC)
re = Solution().minStable([2,4,9,6],1)
print(re)