# https://leetcode.cn/contest/weekly-contest-495/problems/incremental-even-weighted-cycle-queries/
# DSU记录当前合并点到根节点的奇偶性
# 带权并查集
from typing import List, Tuple, Optional



class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n))
        self.dist = [0]*n 
    
    def find(self,i):
        if self.parent[i] ==i:
            return i 
        pi = self.find(self.parent[i])  # 先更新父节点的距离和路径压缩
        self.dist[i] ^= self.dist[self.parent[i]]  # 在用最新父节点的距离
        self.parent[i] = pi 
        return pi 
    
    def union(self,i,j,w):
        pi = self.find(i)
        pj = self.find(j)
        if pi != pj :
            self.parent[pi] = pj 
            self.dist[pi] = self.dist[i]^self.dist[j] ^ w 
            return True
        else:
            return (self.dist[i]^ self.dist[j]) == w 

class Solution:
    def numberOfEdgesAdded(self, n: int, edges: List[List[int]]) -> int:
        ans = 0
        dsu = UnionFind(n)
        for a,b,w in edges:
            if dsu.union(a,b,w):
                ans +=1
        return ans




re =Solution()
print(re)