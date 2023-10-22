from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from collections import Counter
class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        c = Counter(nums)
        ls = list(c.values())
        l,r = 1,min(ls)+1
        #print(r)
        #ls = [18,9]
        #r = min(ls)+1
        def verify(r, a):
            if r ==1:
                return r
            le,ri = (a)//r, (a+r-1-1)//(r-1)
            #print(le,ri,r,a ,"X")
            for b in range(le,-1,-1):
                #print(b)
                if (a- b *(r))%(r-1) == 0:
                    #print(r,a,b,b+  (a- b *(r))//(r-1))
                    return b+  (a- b *(r))//(r-1)
            return 0
        while r:
            isG = True
            cnt = 0
            for a in ls:
                re = verify(r,a)
                #print(r,a,re)
                if re >0:
                    cnt +=re
                else:
                    isG = False
                    break
            if isG == True:
                #print(r,cnt)
                return cnt
            r -=1



re =Solution().minGroupsForValidAssignment([1,1,1,3,1,2,2,2,3])
print(re)