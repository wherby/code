# Verified https://leetcode.cn/problems/shortest-path-in-a-weighted-tree/submissions/622045108/


from typing import List, Tuple

# Python 实现带权路径和查询的可变重链剖分(HLD)
# HLD 通过两次dfs 把树上的点按照链的访问顺序【pos】重排到一维空间，再用线段树等处理 
# 对于线段路径的权重，可以通过权重下放的方式把权重放在低位节点上

from collections import defaultdict

class HLDWithSegmentTree:
    def __init__(self, n, edges, values, root=0):
        """
        初始化带权HLD
        :param n: 节点数量
        :param edges: 树的边列表，格式为[(u, v), ...]
        :param values: 每个节点的初始权值
        :param root: 根节点，默认为0
        """
        self.n = n
        self.root = root
        self.values = values.copy()
        self.adj = defaultdict(list)
        for u, v in edges:
            self.adj[u].append(v)
            self.adj[v].append(u)
        
        # 初始化各种数组
        self.parent = [-1] * n
        self.depth = [0] * n
        self.size = [1] * n
        self.heavy = [-1] * n  # 存储每个节点的重儿子
        
        # 第一次DFS：计算父节点、深度、子树大小和重儿子
        self._dfs1(root)
        
        # 链信息
        self.chain = [i for i in range(n)]  # 每个节点所属的链
        self.head = [i for i in range(n)]   # 每个链的头节点
        self.pos = [0] * n                  # 节点在线性结构中的位置
        
        # 第二次DFS：构建重链
        self.current_pos = 0
        self._dfs2(root)
        
        # 根据HLD顺序重新排列节点值
        self.values_in_hld_order = [0] * n
        for u in range(n):
            self.values_in_hld_order[self.pos[u]] = self.values[u]
        # 构建线段树
        self.segment_tree = SegmentTree(self.values_in_hld_order)
    
    def _dfs1(self, u):
        """第一次DFS，计算size, heavy, parent, depth"""
        max_size = 0
        for v in self.adj[u]:
            if v != self.parent[u]:
                self.parent[v] = u
                self.depth[v] = self.depth[u] + 1
                self._dfs1(v)
                self.size[u] += self.size[v]
                if self.size[v] > max_size:
                    max_size = self.size[v]
                    self.heavy[u] = v
    
    def _dfs2(self, u):
        """第二次DFS，构建重链"""
        self.pos[u] = self.current_pos
        self.current_pos += 1
        
        # 优先处理重儿子，保证重链连续
        if self.heavy[u] != -1:
            v = self.heavy[u]
            self.head[v] = self.head[u]
            self.chain[v] = self.chain[u]
            self._dfs2(v)
        
        # 处理轻儿子，开始新的链
        for v in self.adj[u]:
            if v != self.parent[u] and v != self.heavy[u]:
                self.head[v] = v
                self.chain[v] = v
                self._dfs2(v)
    
    def get_lca(self, u, v):
        """获取两个节点的最近公共祖先(LCA)"""
        while self.chain[u] != self.chain[v]:
            if self.depth[self.head[u]] > self.depth[self.head[v]]:
                u = self.parent[self.head[u]]
            else:
                v = self.parent[self.head[v]]
        return u if self.depth[u] < self.depth[v] else v
    
    def query_path_sum(self, u, v):
        """
        查询u到v路径上的权值和
        """
        res = 0
        while self.chain[u] != self.chain[v]:
            if self.depth[self.head[u]] > self.depth[self.head[v]]:
                # 处理u到head[u]的路径
                res += self.segment_tree.query_sum(self.pos[self.head[u]], self.pos[u])
                u = self.parent[self.head[u]]
            else:
                # 处理v到head[v]的路径
                res += self.segment_tree.query_sum(self.pos[self.head[v]], self.pos[v])
                v = self.parent[self.head[v]]
        
        # 处理最后一条链
        if self.depth[u] > self.depth[v]:
            u, v = v, u
        res += self.segment_tree.query_sum(self.pos[u], self.pos[v])
        return res
    
    def update_node_value(self, u, new_value):
        """
        更新节点的值
        :param u: 要更新的节点
        :param new_value: 新的值
        """
        self.values[u] = new_value
        self.segment_tree.update(self.pos[u], new_value)
    
    def get_pos(self, u):
        """获取节点u在线性结构中的位置"""
        return self.pos[u]
    
    def get_parent(self, u):
        """获取节点u的父节点"""
        return self.parent[u]
    
    def get_depth(self, u):
        """获取节点u的深度"""
        return self.depth[u]
    
    def get_size(self, u):
        """获取以u为根的子树大小"""
        return self.size[u]


class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size <<= 1
        self.tree = [0] * (2 * self.size)
        # 初始化叶子节点
        for i in range(self.n):
            self.tree[self.size + i] = data[i]
        # 构建内部节点
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
    
    def update(self, pos, value):
        """更新位置pos的值为value"""
        pos += self.size
        self.tree[pos] = value
        pos >>= 1
        while pos >= 1:
            new_val = self.tree[2 * pos] + self.tree[2 * pos + 1]
            if self.tree[pos] == new_val:
                break
            self.tree[pos] = new_val
            pos >>= 1
    
    def query_sum(self, l, r):
        """查询区间[l, r]的和"""
        res = 0
        l += self.size
        r += self.size
        while l <= r:
            if l % 2 == 1:
                res += self.tree[l]
                l += 1
            if r % 2 == 0:
                res += self.tree[r]
                r -= 1
            l >>= 1
            r >>= 1
        return res



class Solution:
    def treeQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = n+1 
        adj = []
        g =[[] for _ in range(n)]
        for a,b,c in edges:
            g[a].append(b)
            g[b].append(a)
            adj.append((a,b))
        values = [0]*n 
        levl = [0]*n 

        def dfs(a,parent):
            levl[a] = levl[parent] +1
            for b in g[a]:
                if b != parent:
                    dfs(b,a)
        dfs(1,-1)
        for a,b,c in edges:
            if levl[a] > levl[b]:
                values[a] = c 
            else:
                values[b] = c 
        #print(values)
        hld = HLDWithSegmentTree(n,adj,values,1)
        ans = []
        for query in queries:
            if query[0] ==2:
                ans.append(hld.query_path_sum(query[1],1))
            else:
                _,a,b,c = query
                if levl[a]>levl[b]:
                    a,b = b,a 
                hld.update_node_value(b,c)
        return ans

re = Solution().treeQueries(5,[[1,2,1],[2,3,2],[3,4,3],[4,5,4]],[[2,5],[1,3,4,10],[2,5],[1,4,5,1],[2,5]])
print(re)