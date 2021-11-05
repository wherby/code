from collections import deque
class Solution(object):
    def countSubgraphsForEachDiameter(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        g = [[] for i in range(n)]
        for edg  in edges:
            a,b = edg
            g[a-1].append(b-1)
            g[b-1].append(a-1)
        allow =[0]*n
        A=-1
        res = [0]*n
        def bfs(start,dist, msk):
            q = [start]
            dist[start] = 0
            next= start
            while q:
                cur =q.pop(0)
                for n in g[cur]:
                    if allow[n] ==0:
                        continue
                    if dist[n] ==-1:
                        q.append(n)
                        dist[n] = dist[cur] +1
                        next =n
            return next
                
        for state in range(1,1<<n):
            sn =0
            for i in range(n):
                if (state>>i &1) ==1:
                    allow[i] =1
                    A=i
                    sn+=1
                else:
                    allow[i] =0
            dist = [-1] *n
            B = bfs(A,dist,allow)
            cnt =0
            for d in dist:
                if d != -1:
                    cnt +=1
            if cnt == sn:
                dist = [-1] *n
                C= bfs(B,dist,allow)
                maxDist = max(dist)
                res[maxDist] +=1
        return res[1:]
            


re = Solution().countSubgraphsForEachDiameter(n = 4, edges = [[1,2],[2,3],[2,4]])
print(re)