from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        left =0
        acc =0
        sm = 0
        n = len(nums)
        for i,a in enumerate(nums):
            acc +=dic[a]
            if acc >=k:
                #print(left,i,n-i,acc,dic)
                sm +=n-i
            dic[a] +=1
            while acc>=k and left<i:
                t = dic[nums[left]]
                acc -=t-1
                dic[nums[left]]-=1
                left +=1
                if acc>=k:
                    #print(left,i,n-i,acc,dic)
                    sm +=n-i
        return sm





re =Solution().countGood([2,1,3,1,2,2,3,3,2,2,1,1,1,3,1],11)
print(re)