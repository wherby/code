
from typing import List, Tuple, Optional
from collections import defaultdict,deque
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        dic = defaultdict(list)
        for a,b,t in meetings:
            dic[t].append([a,b])
        p = [i for i in range(n)]
        def findp(a):
            if p[a] != a:
                p[a] =findp(p[a])
            return p[a]
        def union(a,b):
            pa = findp(a)
            pb = findp(b)
            if pa!=pb:
                p[pb]= pa
        union(0,firstPerson)
        tk = list(dic.keys())
        tk.sort()
        for t1 in tk:
            ls = dic[t1]
            cand = set()
            g=defaultdict(list)
            for a,b in ls:
                if findp(a) == findp(0):
                    cand.add(a)
                if findp(b) == findp(0):
                    cand.add(b)
                g[a].append(b)
                g[b].append(a)
            cand = list(cand)
            for a in cand:
                for b in g[a]:
                    if findp(b) != findp(0):
                        union(a,b)
                        cand.append(b)
        ret = []
        for a in range(n):
            if findp(a) == findp(0):
                ret.append(a)
        return ret
            