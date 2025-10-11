# https://leetcode.cn/contest/biweekly-contest-159/problems/kth-smallest-path-xor-sum/submissions/
# 从小merge到大，可以避免长链攻击
# 如果只用有序数组merge，则每个都是N的复杂度
from typing import List, Tuple, Optional

from collections import defaultdict,deque

from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf



class Solution:
    def kthSmallest(self, par: List[int], vals: List[int], queries: List[List[int]]) -> List[int]:
        qd = defaultdict(list)
        for i,(x,k) in enumerate(queries):
            qd[x].append((i,k))
        
        n = len(par)
        g = [[] for _ in range(n)]
        for i,p in enumerate(par):
            if p >= 0:
                g[p].append(i)
        
        m = len(queries)
        res = [-1] *m

            
        def mergeSL(sl1,sl2):
            if len(sl1)<len(sl2):
                sl2,sl1 = sl1,sl2
            for a in sl2:
                if a not in sl1:
                    sl1.add(a)
            return sl1


        def dfs(a,acc):
            cur = vals[a]^acc
            sl  =SortedList([ vals[a]^acc])
            
            for b in g[a]:
                re = dfs(b,cur) 
                sl = mergeSL(sl,re)

            if len(qd[a]) > 0:
                for x,k in qd[a]:
                    if k <= len(sl):
                        res[x] = sl[k-1]
                        #print(a,x,k,sl)
            return sl
        dfs(0,0)
        return res


re =Solution().kthSmallest(par = [-1,0,0], vals = [60839,63555,90182], queries = [[2,2],[0,3]])
print(re)