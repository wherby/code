from typing import List, Tuple, Optional
def TreeMaxPath(g):
    n  = len(g)
    ans=0
    visit =[0]*n
    def dfs(x):
        nonlocal ans
        visit[x] = 1
        for y,c in g[x]:
            if visit[y] : continue
            dfs(y)
            ans = max(ans,d[x] + d[y]  + c)
            d[x] = max(d[x], d[y] + c)
        #print(x, d,ans)
    d =[0]*n
    for i in range(n):
        if visit[i] ==0:
            dfs(i)
    return ans
class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        ls = [0]*(n-1)
        for state in range(1<<n):
            g =[[] for _ in range(n+1)]
            #print(g)
            cnt =0
            
            for a,b in edges:
                a,b = a-1,b-1
                if (1<<a)&state and (1<<b)&state:
                    g[a].append((b,1))
                    g[b].append((a,1))
                    cnt +=1

            if bin(state).count("1") != cnt+1:continue
            ans = TreeMaxPath(g)
            #print(ans,state,g)
            if ans >0:
                ls[ans-1] +=1
        return ls 
    
re =Solution().countSubgraphsForEachDiameter(n = 4, edges = [[1,3],[1,4],[2,3]])
print(re)
            