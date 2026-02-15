
from typing import List, Tuple

# Python 实现带权路径和查询的可变重链剖分(HLD)
# HLD 通过两次dfs 把树上的点按照链的访问顺序【pos】重排到一维空间，再用线段树等处理 
# 对于线段路径的权重，可以通过权重下放的方式把权重放在低位节点上

from collections import defaultdict

class HLDWithSegmentTree:
    def __init__(self, n, edges, values, root=0,op=lambda x,y:x^y):
        """
        初始化带权HLD
        :param n: 节点数量
        :param edges: 树的边列表，格式为[(u, v), ...]
        :param values: 每个节点的初始权值
        :param root: 根节点，默认为0
        """
        self.op = op
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
        self.segment_tree = SegTree(lambda x, y: x ^ y, 0, self.values_in_hld_order)
        
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
                res = self.op(res,self.segment_tree.query_sum(self.pos[self.head[u]], self.pos[u]))
                u = self.parent[self.head[u]]
            else:
                # 处理v到head[v]的路径
                res = self.op(res,self.segment_tree.query_sum(self.pos[self.head[v]], self.pos[v]))
                v = self.parent[self.head[v]]
        
        # 处理最后一条链
        if self.depth[u] > self.depth[v]:
            u, v = v, u
        res = self.op(res,self.segment_tree.query_sum(self.pos[u], self.pos[v]))
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


import typing
def _ceil_pow2(n: int) -> int:
    if n <= 1: return 0
    return (n - 1).bit_length()

class SegTree:
    def __init__(self,
                 op: typing.Callable[[typing.Any, typing.Any], typing.Any],
                 e: typing.Any,
                 v: typing.Union[int, typing.List[typing.Any]]) -> None:
        self._op = op
        self._e = e

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = _ceil_pow2(self._n)
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)

        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p: int) -> typing.Any:
        assert 0 <= p < self._n

        return self._d[p + self._size]

    def prod(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n
        sml = self._e
        smr = self._e
        left += self._size
        right += self._size

        while left < right:
            if left & 1:
                sml = self._op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self._d[right], smr)
            left >>= 1
            right >>= 1

        return self._op(sml, smr)

    def all_prod(self) -> typing.Any:
        return self._d[1]

    def max_right(self, left: int,
                  f: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= left <= self._n
        assert f(self._e)

        if left == self._n:
            return self._n

        left += self._size
        sm = self._e

        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not f(self._op(sm, self._d[left])):
                while left < self._size:
                    left *= 2
                    if f(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    def min_left(self, right: int,
                 f: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= right <= self._n
        assert f(self._e)

        if right == 0:
            return 0

        right += self._size
        sm = self._e

        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not f(self._op(self._d[right], sm)):
                while right < self._size:
                    right = 2 * right + 1
                    if f(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._d[right], sm)

        return 0

    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])
    
    def query_sum(self, left: int, right: int) -> typing.Any:
        """查询区间[left, right]的和"""
        return self.prod(left, right + 1)

    def update(self, p: int, x: typing.Any) -> None:
        """更新位置p的值为x"""
        self.set(p, x)



class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        g = [[] for _ in range(n)]
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        vs = [1 << (ord(c) - ord('a')) for c in s]
        st= HLDWithSegmentTree(n, edges, vs)
        ans = []
        for query in queries:
            q_type, a, b = query.split()
            if q_type == "update":
                u, char = int(a), b
                new_mask = 1 << (ord(char) - ord('a'))
                st.update_node_value(u, new_mask)
            else:
                u, v = int(a), int(b)
                res_mask = st.query_path_sum(u, v)

                ans.append((res_mask & (res_mask - 1)) == 0)
                
        return ans



re =Solution().palindromePath(n = 4, edges = [[0,1],[0,2],[0,3]], s = "abca", queries = ["query 1 2","update 0 b","query 2 3","update 3 a","query 1 3"])
print(re)