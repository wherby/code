
# https://leetcode.cn/problems/maximum-path-quality-of-a-graph/description/?envType=daily-question&envId=2024-07-01
# 需要查找图访问的所以可能，需要用global 变量visit记录访问过的路径，在遍历访问完时回溯状态

from typing import List, Tuple, Optional
class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        n = len(values)
        g= [[] for _ in range(n)]
        for a,b,c in edges:
            g[a].append((b,c))
            g[b].append((a,c))
        mx = 0
        visit={}
        visit[0]=1
        def dfs(a,t,v):
            nonlocal mx
            
            if t > maxTime:
                return
            if a == 0:
                #print(a,t,v,visit)
                mx = max(mx,v)
            for b,c in g[a]:
                if b not in visit:
                    visit[b]=1
                    dfs(b,t+c,v+ values[b])
                    del visit[b]
                else:
                    dfs(b,t+c,v)
                
        dfs(0,0,values[0])
        return mx

#re = Solution().maximalPathQuality(values = [0,32,10,43], edges = [[0,1,10],[1,2,15],[0,3,10]], maxTime = 49)       
re = Solution().maximalPathQuality(values = [1,2,3,4], edges = [[0,1,10],[1,2,11],[2,3,12],[1,3,13]], maxTime = 50)
#re =Solution().maximalPathQuality(values = [100000000,100000000,100000000,100000000,100000000,100000000,100000000,100000000,100000000,100000000], edges = [[0,1,10],[1,2,10],[2,3,10],[3,4,10],[4,5,10],[5,6,10],[6,7,10],[7,8,10],[8,9,10],[0,9,10]], maxTime = 100)
print(re)
            
        