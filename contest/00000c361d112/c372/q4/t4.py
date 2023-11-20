from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList



class Solution:
    def leftmostBuildingQueries(self, hs: List[int], queries: List[List[int]]) -> List[int]:
        n = len(hs)
        st=[]
        ret = [-1]*len(queries)
        dic =defaultdict(list)
        for idx,(a,b) in enumerate(queries):
            a,b = min(a,b),max(a,b)
            if hs[a]<hs[b]:
                ret[idx] = b 
            elif a ==b:
                ret[idx] = a 
            else:
                dic[b].append((a,idx))
        #print(dic)
        for i,a in enumerate(hs[::-1]):
            #print(i,a)
            while st and hs[st[-1]]<a :
                st.pop()
            st.append(n-1-i)
            #print(st)
            for c,idx in dic[n-1-i]:
                
                if hs[st[0]]<=hs[c]:
                    continue
                l,r = 0,len(st)-1
                while l <r:
                    mid = (l+r+1)>>1
                    if hs[st[mid]]>hs[c]:
                        l= mid
                    else:
                        r = mid-1
                ret[idx] = st[l]
                
                
        return ret





re =Solution().leftmostBuildingQueries(hs = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]])
print(re)