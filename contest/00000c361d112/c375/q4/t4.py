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
        for vs in dic.values():
            l,r  =vs[0],vs[-1]
            #print(l,r)
            lidx = sl.bisect_left((l,l))
            if l <sl[lidx][0]:
                lidx -=1
            ridx = sl.bisect_left((r+1,r+1))
            rm = []
            rl = sl[lidx][0]
            rr = sl[ridx][0]-1 if ridx <len(sl) else n
            for i in range(lidx,ridx):
                rm.append(sl[i])
            for a in rm:
                sl.remove(a)
            if rl <= rr:
                sl.add((rl,rr))
            #print(sl)
        #print(sl)
        return quickPow(2,len(sl)-1)




re =Solution().numberOfGoodPartitions(nums = [1,5,1,5,6])
print(re)