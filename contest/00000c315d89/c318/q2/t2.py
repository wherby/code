from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
#from sortedcontainers import SortedDict,SortedList
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        mx = 0
        n = len(nums)
        acc = 0
        dic = defaultdict(int)
        for i in range(k):
            acc += nums[i]
            dic[nums[i]]+=1
        if len(dic) == k:
            mx = acc
        for j in range(k,n):
            acc += nums[j] - nums[j-k]
            dic[nums[j]] +=1
            dic[nums[j-k]]-=1
            if dic[nums[j-k]] == 0:
                del dic[nums[j-k]]
            if len(dic) == k:
                mx = max (mx,acc)
        return mx




re =Solution().maximumSubarraySum(nums = [1,5,4,2,9,9,9], k = 3)
print(re)