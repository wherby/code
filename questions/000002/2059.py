from typing import List, Tuple, Optional




class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        sm = 0 
        g = [[] for _ in range(n)]
        def dfs(i,res,p):
            if dp.get(i,10**10) <= res:
                return
            dp[i] = min(dp.get(i,10**10),res)
            for a,c in g[i]:
                if a ==p or a not in ls:continue
                dfs(a,dp[i]+c,i)
            
        for a,b,c in roads:
            g[a].append((b,c))
            g[b].append((a,c))
        for state in range(1<<n):
            ls = set()
            for i in range(n):
                if (1<<i)&state:
                    ls.add(i)
            if len(ls) == 0:
                sm +=1
            else:
                isG = True
                for i in ls:
                    dp = {}
                    dfs(i,0,-1)
                    #print(len(visit),i,len(ls))
                    
                    if len(dp) != len(ls) or max(dp.values()) > maxDistance:
                        #print(len(dp),len(ls),ls,dp, max(dp.values()))
                        #print(state, isG,visit,ls)
                        isG  = False
                        break
                if isG:
                    #print(state)
                    sm +=1
        return sm



re =Solution().numberOfSets(n = 5, maxDistance = 25, roads = [[1,0,17],[1,0,1],[2,1,24],[3,2,12],[1,0,7],[3,2,4],[2,1,15],[0,4,14]])
print(re)