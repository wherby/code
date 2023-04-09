from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        dic = defaultdict(list)
        for i,a in enumerate(nums):
            dic[a].append(i)
        n = len(nums)
        ret = [0]*n
        for k,ls in dic.items():
            
            pls =[0]
            for a in ls:
                pls.append(pls[-1] +a)
            m =len(ls)
            for i in range(len(ls)):
                acc = ls[i]*(i+1)-  pls[i+1] + pls[-1] -pls[i+1] - ls[i]*(m-1-i)
                ret[ls[i]]=acc
        return ret





re =Solution().distance(nums = [1,3,1,1,2])
print(re)