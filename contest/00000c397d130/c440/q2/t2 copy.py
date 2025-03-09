from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf

class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        ls= [(a,i) for i,a in enumerate(nums1)]
        ls.sort()
        n = len(nums1)
        ret = [0]*n
        sl = SortedList()
        acc = 0
        dic=defaultdict(int)
        st=[]
        for idx,(a,i) in enumerate(ls):
            if dic[a] ==0:
                for b in st:
                    sl.add(b)
                    acc +=b 
                st = []
                while len(sl) > k:
                    acc -=sl[0]
                    sl.pop(0)
            dic[a] +=1
            st.append(nums2[i])
            ret[i]=acc
        return ret
            




re =Solution().findMaxSum(nums1 = [4,2,1,5,3], nums2 = [10,20,30,40,50], k = 2)
print(re)