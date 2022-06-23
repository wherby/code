# BFS
# https://leetcode-cn.com/problems/minimum-height-trees/
from collections import deque
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        mx = n 
        ls =[[] for _ in range(n)]
        ins = [0]*n
        for a,b in edges:
            ls[a].append(b)
            ls[b].append(a)
            ins[a] +=1
            ins[b] +=1
        dp =[n]*n
        def bfs(g,stp):
            n = len(g)
            visited =[0]*n
            st =deque([(stp,0)])
            ret = []
            while st:
                p,layer = st.popleft()
                visited[p] =1
                for a in g[p]:
                    if visited[a]:continue
                    st.append((a,layer+1))
                ret.append((p,layer))
            return ret
        ret1 = bfs(ls,0)
        lsp = ret1[-1][0]
        ret2= bfs(ls,lsp)
        ret3 =bfs(ls,ret2[-1][0])
        dic = {}
        for p,d in ret3:
            dic[p] =d
        #print(ret2)
        mx = ret2[-1][1]
        if mx %2 ==0:
            targ =[mx //2 ]
        else:
            targ =[mx//2,mx//2+1]
        res =[]
        for p,d in ret2:
            if d in targ and dic[p] + d ==mx:
                res.append(p)
        return res

re = Solution().findMinHeightTrees(8,[[0,1],[1,2],[2,3],[0,4],[4,5],[4,6],[6,7]])
print(re)
        
