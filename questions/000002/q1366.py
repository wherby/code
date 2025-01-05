from typing import List, Tuple, Optional
from collections import defaultdict,deque
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes[0])
        m = len(votes)
        cand = {}
        for a  in votes[0]:
            cand[a] =0 
        for i in range(n):
            tmp = defaultdict(int)
            for j in range(m):
                tmp[votes[j][i]] +=1
            dic ={}
            
            for  k in cand:
                dic[k] = cand[k]*(m+2) + tmp[k]
            vs =list(set( dic.values()))
            vs.sort()
            hs ={}
            #print(vs)
            for j,a in enumerate(vs):
                hs[a] = j
            for k,v in dic.items():
                cand[k] = hs[v]
            #print(i,cand)
        ls = []
        for k,v in cand.items():
            ls.append((-v,k))
        ls.sort()
        return "".join([a[1] for a in ls])
        
    

re =Solution().rankTeams(["ZMNAGUEDSJYLBOPHRQICWFXTVK"])
print(re)

        
