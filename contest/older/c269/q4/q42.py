import heapq
import math
class Solution(object):
    def findAllPeople(self, n, meetings, firstPerson):
        visited = [0]*n
        findT = [math.inf] *n
        findT[0] =findT[firstPerson] =0
        stack = []
        heapq.heappush(stack,(0,0))
        heapq.heappush(stack,(0,firstPerson))
        g = [[] for _ in range(n)]
        for a,b,t in meetings:
            g[a].append( [b,t])
            g[b].append([a,t])
        while stack:
            t,a = heapq.heappop(stack)
            if visited[a] ==1:
                continue
            visited[a] =1
            #print(g[a],a)
            for b,t1 in g[a]:
                if t1 >= t and t1 < findT[b]:
                    findT[b] = t1
                    heapq.heappush(stack,(t1,b))
        res =[]
        for i in range(n):
            if findT[i] != math.inf:
                res.append(i)
        return res

n=12
m=[[10,8,6],[9,5,11],[0,5,18],[4,5,13],[11,6,17],[0,11,10],[10,11,7],[5,8,3],[7,6,16],[3,6,10],[3,11,1],[8,3,2],[5,0,7],[3,8,20],[11,0,20],[8,3,4],[1,9,4],[10,7,11],[8,10,18]]
f=9
re = Solution().findAllPeople(n,m,f)
print(re)

