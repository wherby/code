from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
from collections import defaultdict,deque
from collections import defaultdict,deque
class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.size = [1] * n
        self.part = n

    def find(self, x):
        if x != self.root[x]:
            # 在查询的时候合并到顺带直接根节点
            root_x = self.find(self.root[x])
            self.root[x] = root_x
            return root_x
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        if self.size[root_x] >= self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.root[root_x] = root_y
        self.size[root_y] += self.size[root_x]
        # 将非根节点的秩赋0
        self.size[root_x] = 0
        self.part -= 1
        return True

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def get_root_part(self):
        # 获取每个根节点对应的组
        part = defaultdict(set)
        n = len(self.root)
        for i in range(n):
            part[self.find(i)].add(i)
        return part

    def get_root_size(self):
        # 获取每个根节点对应的组大小
        size = defaultdict(int)
        n = len(self.root)
        for i in range(n):
            size[self.find(i)] = self.size[self.find(i)]
        return size
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        n = len(queries)
        qls= []
        for i,a in enumerate(queries):
            qls.append((a,i))
        qls.sort()
        m,n = len(grid),len(grid[0])
        st =[]
        for i in range(m):
            for j in range(n):
                heapq.heappush(st,(grid[i][j],i,j))
        dsu=UnionFind(m*n)
        ans = [0]*len(queries)
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        visit={}
        for q,idx in qls:
            while st and st[0][0]<q:
                a,x,y = heapq.heappop(st)
                for dx,dy in dir:
                    nx,ny = x+dx,y+dy 
                    if 0<=nx<m and 0<=ny<n and (nx,ny) in visit :
                        if dsu.find(x *n +y) != dsu.find(nx*n +ny):
                            dsu.union(x *n +y, nx*n +ny)
                visit[(x,y)] =1
            if (0,0) in visit:
                ans[idx] = dsu.size[dsu.find(0)]
            #print(q,idx,visit)
        return ans
                
        




re =Solution().maxPoints(grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2])
print(re)