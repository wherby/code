
# 
https://leetcode.cn/problems/longest-cycle-in-a-graph/

``` python
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        ans = -1
        cur_time = 1  # 当前时间
        vis_time = [0] * n  # 首次访问 x 的时间
        for x in range(n):
            start_time = cur_time  # 本轮循环的开始时间
            while x != -1 and vis_time[x] == 0:  # 没有访问过 x
                vis_time[x] = cur_time  # 记录访问 x 的时间
                cur_time += 1
                x = edges[x]  # 访问下一个节点
            #print(vis_time,x,start_time,vis_time[x])
            if x != -1 and vis_time[x] >= start_time:  # x 在本轮循环中访问了两次，说明 x 在环上
                ans = max(ans, cur_time - vis_time[x])  # 前后两次访问 x 的时间差，即为环长
        #print(vis_time)
        return ans  # 如果没有找到环，返回的是 ans 的初始值 -1
```

```python 
#  用idx 判定每次循环
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        g = [[] for _ in range(n) ]
        ind = [0]*n 
        for a,b in enumerate(edges):
            if b == -1:
                continue
            g[a].append(b)
            ind[b] +=1
        visit =[(-1,-1)] *n 
        ret = -1 

        def dfs(a,acc,idx):
            if visit[a][0] != -1 and visit[a][1] ==idx:
                return acc -visit[a][0] 
            elif visit[a][1] != -1:
                return -1
            visit[a] = (acc,idx) 
            ret = -1 
            for b in g[a]:
                ret = dfs(b,acc+1,idx)
            return ret 
        idx = 0
        for i in range(n):
            if visit[i][0] ==-1 and ind[i] ==0 :
                idx +=1
                ret = max(ret , dfs(i,0,idx))
                #print(visit,ret,i)
        for i in range(n):
            if visit[i][0] ==-1:
                idx +=1
                ret = max(ret , dfs(i,0,idx))
            
        return ret  
```