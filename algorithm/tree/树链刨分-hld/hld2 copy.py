#   https://leetcode.cn/problems/shortest-path-in-a-weighted-tree/submissions/622045108/
# Not verified for funcitonal segment tree which maybe used to handle max min value beside sum in paths

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
                res += self.segment_tree.query(self.pos[self.head[u]], self.pos[u])
                u = self.parent[self.head[u]]
            else:
                # 处理v到head[v]的路径
                res += self.segment_tree.query(self.pos[self.head[v]], self.pos[v])
                v = self.parent[self.head[v]]
        
        # 处理最后一条链
        if self.depth[u] > self.depth[v]:
            u, v = v, u
        res += self.segment_tree.query(self.pos[u], self.pos[v])
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


from math import ceil, log2

class SegmentTree:
    # merge(left, right): function used to merge the two halves
    # basef(value): function applied on individual values
    # basev: identity for merge function, merger(value, basev) = value 
    # update(node_value, old, new): function to update the nodes
    def __init__(self, array, merge=lambda x,y:x+y, basev = 0, basef=lambda x:x):
        self.merge = merge
        self.basef = basef
        self.basev = basev
        self.n = len(array)
        self.array = array
        self.tree = [0] * ( 2**ceil(log2(len(array))+1) - 1 )
        self.build(array)
    
    def __str__(self):
        return ' '.join([str(x) for x in self.tree])

    def _build_util(self, l, r, i, a):
        if(l==r):
            self.tree[i] = self.basef(a[l])
            return self.tree[i]
        mid = (l+r)//2
        self.tree[i] = self.merge(self._build_util(l,mid, 2*i+1, a), self._build_util(mid+1, r, 2*i+2, a))
        return self.tree[i]

    def build(self, a):
        self._build_util(0, len(a)-1, 0, a)

    def _query_util(self, i, ln, rn, l, r):
        if ln>=l and rn<=r:
            return self.tree[i]
        if ln>r or rn<l:
            return self.basev
        return self.merge( self._query_util( 2*i+1, ln, (ln+rn)//2, l, r ), self._query_util( 2*i+2, (ln+rn)//2+1, rn, l, r ) )

    def query(self, l, r):
        return self._query_util( 0, 0, self.n-1, l, r )

    def _update_util(self, i, ln, rn, x, v):
        if x>=ln and x<=rn:
            if ln != rn:
                self._update_util( 2*i+1, ln, (ln+rn)//2, x, v )
                self._update_util( 2*i+2, (ln+rn)//2 + 1, rn, x, v )
                self.tree[i] = self.merge(self.tree[2*i+1], self.tree[2*i+2])
            else:
                self.tree[i] = self.basef(v)

    def update(self, x, v):
        self._update_util( 0, 0, self.n-1, x, v )   
        self.array[x] =v    



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