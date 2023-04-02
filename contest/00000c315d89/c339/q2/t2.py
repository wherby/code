from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        dic = defaultdict(int)
        for a in nums:
            dic[a]+=1
        res = []
        keys =list(dic.keys())
        cnt = max(dic.values())
        for _ in range(cnt):
            tmp =[]
            for k in keys:
                if dic[k]>0:
                    tmp.append(k)
                    dic[k] -=1
            res.append(tmp)
        return res
            





re =Solution()
print(re)