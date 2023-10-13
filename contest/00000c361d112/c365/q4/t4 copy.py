from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        ret = [-1]*n
        visit ={}
        st=[]
        def dfs(a):
            sst =[]
            sst.append(a)
            while sst:
                a = sst.pop()
                if a not in visit:
                    visit[a] = 1
                    st.append(a)
                    sst.append(edges[a])
                else:
                    if ret[a]==-1:
                        cir =[]
                        cnt = 0
                        while st[-1]!=a:
                            cir.append(st[-1])
                            st.pop()
                            cnt +=1
                        cir.append(st[-1])
                        st.pop()
                        cnt +=1
                        for a in cir:
                            ret[a] = cnt
                    while st:
                        a = st.pop()
                        ret[a] = ret[edges[a]] +1
        for i in range(n):
            dfs(i)
        return ret





re =Solution().countVisitedNodes(edges = [1,2,0,0])
print(re)