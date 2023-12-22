# https://leetcode.cn/contest/weekly-contest-376/problems/minimum-cost-to-make-array-equalindromic/
# https://leetcode.cn/problems/find-the-closest-palindrome/solutions/1303241/python-tan-xin-da-mo-ni-by-himymben-6cbl/

from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf

class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        l,r = 1,n
        pre = [0] 
        for a in nums:
            pre.append(a+pre[-1])
        #$print(pre)
        def verify(l):
            if l %2 ==0:
                for i in range(n-l+1):
                    midV = (nums[(l-1)//2 + i] + nums[(l//2+i)])//2
                    p1 = midV*(l//2) - pre[l//2+i] + pre[i]
                    p2 = pre[l+i] -pre[l//2+i] - midV*(l//2)
                    if p1+p2 <=k:
                        return True
                return False
            else:
                for i in range(n-l+1):
                    midV = nums[l//2+i]
                    p1 = midV*(l//2) - pre[l//2+i] + pre[i]
                    p2 = pre[l+i] -pre[l//2+i] - midV*(l//2 +1)
                    #print(i,p1,p2,midV,pre[l+i] ,pre[l//2+i] , midV*(l//2 +1))
                    if p1+p2 <=k:
                        return True
                return False
        while l<r:
            mid =(l+r+1)>>1
            #print(mid)
            if verify(mid):
                l = mid 
            else:
                r = mid-1
        return l



re =Solution().maxFrequencyScore(nums = [1,4,4,2,4], k = 0)
print(re)