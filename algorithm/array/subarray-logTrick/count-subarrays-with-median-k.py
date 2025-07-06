# https://leetcode.cn/problems/count-subarrays-with-median-k/
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        kIdx = nums.index(k)
        
        left =nums[:kIdx]
        right = nums[kIdx+1:]
        dicLeft =defaultdict(int)
        acc= 0
        dicLeft[0]+=1
        for a in left[::-1]:
            if a >k:
                acc +=1
            else:
                acc -=1
            dicLeft[acc] +=1
        #print(dicLeft)
        cnt =0
        acc =0
        for i in range(kIdx,n):
            if nums[i]< k:
                acc +=1
            elif nums[i]>k:
                acc -=1
            cnt += dicLeft[acc]
            cnt += dicLeft[acc+1]
            #print(nums[i],cnt)
        return cnt
        
                



re =Solution().countSubarrays(nums = [3,2,1,4,5], k = 4)
print(re)
re =Solution().countSubarrays(nums = [2,3,1], k = 3)
print(re)
re =Solution().countSubarrays([2,5,1,4,3,6],1)
print(re)