from typing import List, Tuple, Optional
import heapq
class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        st =[(-1,0,-1)]
        visited ={}
        g =[[] for _ in range(n)]
        res ={}
        for a,b,x in edges:
            g[a].append([b,x])
            g[b].append([a,x])
            res[(max(a,b),min(a,b))] = x
        cnt =0
        while st:
            cst,a,p = heapq.heappop(st)
            if a in visited:continue
            visited[a] =1
            cnt +=1
            cst +=1
            for b,x in g[a]:
                if b ==p:continue
                if x + cst+1 >maxMoves:
                    k = min(maxMoves-cst,res[(max(a,b),min(a,b))])
                    cnt +=k
                    res[(max(a,b),min(a,b))] -= k
                else:
                    k = min(maxMoves-cst,res[(max(a,b),min(a,b))])
                    res[(max(a,b),min(a,b))] -= k
                    cnt +=k
                    heapq.heappush(st,[cst+k,b,a])
        return cnt 

re =Solution().reachableNodes([[0,2,3],[0,4,4],[2,3,8],[1,3,5],[0,3,9],[3,4,6],[0,1,5],[2,4,6],[1,2,3],[1,4,1]],8,5)
print(re)