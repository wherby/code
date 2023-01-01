from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        s= s+s
        dic = defaultdict(int)
        pls=[[0,0,0]]
        for i,a in enumerate(s):
            dic[a] +=1
            pls.append([dic['a'],dic['b'],dic['c']])
        l,r = -1,n
        def verify(mid):
            for i in range(n-mid,n+1):
                a= pls[i+mid]
                b = pls[i]
                #print(a,b,i,i+mid-1)
                if a[0]-b[0]>=k and a[1]-b[1]>=k and a[2]-b[2]>=k:
                    return True
            return False
        while l < r:
            mid = (l+r)>>1
            #print(l,r,mid)
            if verify(mid):
                #print(mid)
                r = mid 
            else:
                l=mid +1
        return l if verify(l) else -1
                




re =Solution().takeCharacters(s = "accccc", k =1)
print(re)