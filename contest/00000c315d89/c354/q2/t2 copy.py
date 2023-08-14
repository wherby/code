from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        mxL = max(max(nums),k,200)
        ls = [0]*(mxL*3+100)
        offset = mxL
        for a in nums:
            #print(a,k,offset)
            ls[offset + a -k] +=1
            ls[offset + a +k+1] -=1
        acc = 0 
        mx = 0
        for i in range(mxL*3+100): 
            acc += ls[i]
            mx = max(mx,acc)
        #print(ls[offset-10:offset+10])
        return mx




re =Solution().maximumBeauty([866,436,295,697,747,731,444,705,689,651,543,213,700,872,708,306,912,704,879,365,785,750,73,276,201,102,278,232,657,477,975,754,640,840,702,832,585,573,543,834,475,600,848],919)
print(re)