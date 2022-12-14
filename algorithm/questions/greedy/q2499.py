# https://leetcode.cn/contest/biweekly-contest-93/problems/minimum-total-cost-to-make-arrays-unequal/
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dic1= defaultdict(int)
        cnt,res =0,0
        for i,(a,b) in enumerate(zip(nums1,nums2)):
            if a ==b:
                res +=i
                cnt +=1
                dic1[a] +=2
        fd = True
        for k,v in dic1.items():
            if v <=cnt :continue
            fd = False
            for i in range(n):
                if nums1[i] != nums2[i] and nums1[i] != k and nums2[i] != k:
                    cnt +=1
                    res +=i 
                if cnt >= v:
                    fd = True
                    break
        return res if fd else -1 
        
        





re =Solution().minimumTotalCost(nums1 = [1,2,3,4,5], nums2 = [1,2,3,4,5])
print(re)