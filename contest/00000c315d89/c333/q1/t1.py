from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dic = defaultdict(int)
        num = nums1 +nums2
        for a in num:
            dic[a[0]] += a[1]
        res =[]
        for k,v in dic.items():
            res.append([k,v])
        res.sort()
        return res
        



re =Solution().mergeArrays(nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]])
print(re)