# https://leetcode.cn/contest/weekly-contest-346/problems/modify-graph-edge-weights/
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        def verify(k,sor):
            g = [[] for _ in range(n)]
            for a,b,c in edges:
                if c <0:
                    c = k
                g[a].append((b,c))
                g[b].append((a,c))
            st = [(0,sor)]
            visit = {}
            while st:
                c,d = heapq.heappop(st)
                if d in visit:continue
                visit[d] =c
                #if c > target: continue
                for b,c1 in g[d]:
                    if b not in visit:
                        heapq.heappush(st,(c+c1,b))
            return visit 
        g = [[] for _ in range(n)]
        for a,b,c in edges:
            if c <0:
                c = 1
            g[a].append((b,c,len(g[b]),len(g[a])))
            g[b].append((a,c,len(g[a])-1,len(g[b])))
        vis1 = verify(1,source)
        vis2 = verify(1,destination)
        vis3 = verify(2*10**9,source)
        if vis1[destination]>target or vis3[destination] <target:
            return []
        spg = {}
        medge = []
        for i,(a,b,c) in enumerate(edges):
            if c == -1:
                spg[(a,b)] =(1,i)
                spg[(b,a)] =(1,i)
                c = 1 
            medge.append([a,b,c])
        st = [(0,source)]
        visit ={}
        #print(vis1,vis2,spg)
        #print(medge)
        while st:
            c,a = heapq.heappop(st)
            if a in visit:continue
            #print(c+vis2[a],a,c,medge)
            visit[a] =c
            for b,c1,id1,id2 in g[a]:
                if b not in visit: 
                    if (a,b) in spg :
                        v,idx = spg[(a,b)]
                        if target-c - vis2[b] <c1:continue
                        medge[idx] =[medge[idx][0],medge[idx][1],target-c - vis2[b]] 
                        #print(b,target,a,c,vis1[b],(a,b ,target-c - vis2[b]))
                        g[a][id2] =[b,target-c - vis2[b],g[a][id2][2],g[a][id2][3]]
                        g[b][id1] =[a,target-c - vis2[b],g[b][id1][2],g[b][id1][3]]
                        heapq.heappush(st,(c + medge[idx][2],b))
                    else:
                        heapq.heappush(st,(c+c1,b))
        #print(visit,medge)
        if visit[destination] == target:
            return medge
        return []




#re =Solution().modifiedGraphEdges(4,[[0,1,-1],[1,2,-1],[3,1,-1],[3,0,2],[0,2,5]],2,3,8)
#re =Solution().modifiedGraphEdges(5,[[0,2,5],[2,1,-1],[2,4,3],[3,4,5],[4,0,1],[0,3,-1],[2,3,-1]],0,1,9)
re =Solution().modifiedGraphEdges(n = 4, edges = [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]], source = 0, destination = 2, target = 6)
print(re)

## 
#    5    5
# 0----2----1  
#       --------4
#  --------3----
#       7    5
#  -------------
#     1