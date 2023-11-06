from collections import deque
class Solution(object):
    def networkBecomesIdle(self, edges, patience):
        """
        :type edges: List[List[int]]
        :type patience: List[int]
        :rtype: int
        """
        n = len(patience)
        visited =[0] *n
        g = [[] for i in range(n)]
        cost = [0]*n
        for e in edges:
            a,b = e
            g[a].append(b)
            g[b].append(a)
        bfs = deque([[0,0]])
        #print(g)
        while bfs:
            r,c = bfs.popleft()
            visited[r] = 1
            for t in g[r]:
                if visited[t] ==0:
                    bfs.append([t,c+1])
            if cost[r] == 0:
                cost[r] =c
        #print(cost)
        for i in range(1,n):
            cost[i] = cost[i] *2
            if cost[i] >=patience[i] :
                cost[i] = cost[i]*2  - (cost[i] -1)%patience[i]
            else:
                cost[i] +=1
        #print(cost)
        return max(cost)



edges = [[5,7],[15,18],[12,6],[5,1],[11,17],[3,9],[6,11],[14,7],[19,13],[13,3],[4,12],[9,15],[2,10],[18,4],[5,14],[17,5],[16,2],[7,1],[0,16],[10,19],[1,8]]


patience = [0,2,1,1,1,2,2,2,2,1,1,1,2,1,1,1,1,2,1,1]
re = Solution().networkBecomesIdle(edges,patience)
print(re)

