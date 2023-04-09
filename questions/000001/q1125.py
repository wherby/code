from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        dic ={a:i for i,a in enumerate(req_skills)}
        m = len(req_skills)
        n = len(people)
        
        pls =[0]*n 
        for i in range(n):
            acc = 0
            for p in people[i]:
                acc = acc | (1<<dic[p])
            pls[i] =acc
        cands = [[] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if pls[j] &(1<<i):
                    cands[i].append(j)
        res = []
        dic ={}
        @cache
        def dfs(st):
            if st ==(1<<m)-1:
                return 0
            ret = n 
            cc = -1
            for i in range(m):
                if st &(1<<i) == 0:
                    cand = cands[i]
                    for c in cand:
                        val= 1+dfs(st|pls[c])
                        if val < ret:
                            ret = val
                            cc =c 
                    break
            dic[st]=cc
            return ret
        dfs(0)
        st =0 
        while st != (1<<m) -1:
            res.append(dic[st])
            st = st | pls[dic[st]]
        return list(res)

req_skills=["algorithms","math","java","reactjs","csharp","aws"]
people=[["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]

re = Solution().smallestSufficientTeam(req_skills , people )
print(re)