from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf
from collections import Counter


mod = 10**9 +7
def quickPow(x,y):
    ret =1
    cur = x 
    while y >0:
        if y & 1:
            ret = ret * cur % mod
        cur = cur *cur % mod
        y = y //2
    return ret

class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        dic = defaultdict(list)
        for i,a  in enumerate(nums):
            dic[a].append(i)
        n = len(nums)
        sl = [(i,i) for i in range(n)]
        sl = SortedList(sl)
        #print(dic)
        for vs in dic.values():
            l,r  =vs[0],vs[-1]
            rm = []
            lidx  = sl.bisect_left((l,l))
            if lidx >= len(sl) or sl[lidx][0] >l:
                lidx -=1
            left = sl[lidx][0]
            right = sl[lidx][1]
            while lidx < len(sl) and sl[lidx][1]<=r:
                rm.append(sl[lidx])
                right = sl[lidx][1]
                lidx +=1
            #print(rm,l,r)
            for a in rm:
                sl.remove(a)
            if len(rm)>0:
                sl.add((left,right))
            #print(sl)
        return quickPow(2,len(sl)-1)




re =Solution().numberOfGoodPartitions(nums = [2,4,2,7,4])
print(re)