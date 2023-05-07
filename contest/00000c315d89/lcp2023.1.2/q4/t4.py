from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def evolutionaryRecord(self, parents: List[int]) -> str:
        n  = len(parents)
        cd = [[] for i in range(n)]
        for i,a in enumerate(parents):
            if a != -1:
                cd[a].append(i)
        dp = [[] for _ in range(n)]
        def dfs(i):
            if len(cd[i]) ==0:
                return ""
            re= []
            for a in cd[i]:
                re.append("0" + dfs(a)+"1")
            re.sort()
            return "".join(re)
        ret = dfs(0)
        st = []
        for a in ret:
            st.append(a)
        while st and st[-1] =="1":
            st.pop()
        return "".join(st)





re =Solution().evolutionaryRecord(parents = [-1,0,0,1,2,2])
print(re)