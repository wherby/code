from typing import List, Tuple, Optional

from functools import cache


from bisect import bisect_right,insort_left,bisect_left

import itertools
class Solution:
    def minMergeCost(self, lists: List[List[int]]) -> int:

        n = len(lists)
        acc =0
        @cache
        def getMd(sa):
            nonlocal acc 
            #print(sa)
            acc+=1
            la=[]
            for i in range(n):
                if (1<<i) &sa:
                    la.append(i)
            m = 0 
            for a in la:
                m +=len(lists[a])
            l = min(lists[a][0] for a in la)
            r = max(lists[a][-1] for a in la)
            while l <r:
                #print(l,r)
                md = (l+r)//2 
                cnt =0
                for a in la:
                    cnt += bisect_right(lists[a] ,md)
                if cnt >= (m+1)//2:
                    r = md 
                else:
                    l = md+1
            #print(m,l,cnt,la)
            return m,l

        @cache 
        def dfs(state):
            res = 10**30
            la  = []
            for i in range(n):
                if (1<<i) & state:
                    la.append(i)
            if len(la) ==1:
                return 0
            m = len(la)
            m = m //2
            cand =[]
            
            for i in range(1,m+1):
                ls = itertools.combinations(la,i)
                for l1 in ls:
                    acc = 0 
                    for b in l1:
                        acc +=1<<b
                    cand.append(acc)
            #print(m,cand,state,la)
            for c1 in cand:
                l1,v1 = getMd(c1)
                l2,v2 = getMd(state-c1)
                #print(c1,state-c1,v1,v2,l1,l2,"a")
                res = min(res,dfs(c1) + dfs(state-c1) + l1+l2 +abs(v1-v2))

            
                    
            return res 
        n = len(lists)
        return dfs((1<<n) -1)

                        

                    


from input import lists,lists2

#lists = [[3,10],[1,3,8]]

re =Solution().minMergeCost([[1,3,5],[2,4],[6,7,8]])
print(re)