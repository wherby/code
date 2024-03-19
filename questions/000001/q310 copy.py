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
        ls =[[] for _ in range(n)]
        ins = [0]*n
        for a,b in edges:
            ls[a].append(b)
            ls[b].append(a)
            ins[a] +=1
            ins[b] +=1
        heigh = [0]*n
        cand = []
        for i in range(n):
            if ins[i] ==1:
                cand.append(i)
        lev =1
        while cand:
            tmp = []
            for a in cand:
                heigh[a] =lev
                for b in ls[a]:
                    ins[b] -=1
                    if ins[b] == 1:
                        tmp.append(b)
            lev +=1
            cand = tmp
        mx = max(heigh)
        return [i for i,a in enumerate(heigh) if a ==mx]

re = Solution().findMinHeightTrees(8,[[0,1],[1,2],[2,3],[0,4],[4,5],[4,6],[6,7]])
print(re)
        
