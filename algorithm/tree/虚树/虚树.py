

import sys

# 处理树深度较大的情况
sys.setrecursionlimit(300000)

class VirtualTreeHelper:
    def __init__(self, n, adj):
        self.n = n
        self.adj = adj
        self.dfn = [0] * n
        self.ts = 0
        self.dep = [0] * n
        self.mx = n.bit_length()
        # pa[v][i] 表示 v 的第 2^i 个祖先
        self.pa = [[-1] * self.mx for _ in range(n)]
        
        # 虚树专用的邻接表和标记
        self.vt = [[] for _ in range(n)]
        self.is_critical = [-1] * n
        
        self._precompute(0, -1, 0)
        self._init_spares_table()

    def _precompute(self, v, p, d):
        """预处理 DFN 序、深度和直接父节点"""
        self.dfn[v] = self.ts
        self.ts += 1
        self.dep[v] = d
        self.pa[v][0] = p
        for w in self.adj[v]:
            if w != p:
                self._precompute(w, v, d + 1)

    def _init_spares_table(self):
        """倍增预处理祖先"""
        for i in range(self.mx - 1):
            for v in range(self.n):
                p = self.pa[v][i]
                if p != -1:
                    self.pa[v][i+1] = self.pa[p][i]
                else:
                    self.pa[v][i+1] = -1

    def get_lca(self, v, w):
        """倍增求 LCA"""
        if self.dep[v] > self.dep[w]:
            v, w = w, v
        
        # 先跳到同一深度
        diff = self.dep[w] - self.dep[v]
        for i in range(diff.bit_length()):
            if (diff >> i) & 1:
                w = self.pa[w][i]
        
        if v == w:
            return v
        
        # 倍增往上跳
        for i in range(self.mx - 1, -1, -1):
            if self.pa[v][i] != self.pa[w][i]:
                v, w = self.pa[v][i], self.pa[w][i]
        return self.pa[v][0]

    def build_virtual_tree(self, nodes, current_val):
        """
        根据给定的关键节点列表构建虚树
        nodes: 关键节点的索引列表
        current_val: 当前处理的组别标识
        """
        # 按照 DFN 序排序，这是构建虚树的前提
        nodes.sort(key=lambda x: self.dfn[x])
        
        root = 0
        self.vt[root] = []
        stack = [root]
        
        # 标记关键节点
        for v in nodes:
            self.is_critical[v] = current_val
            if v == root: continue
            self.vt[v] = []
            
            lca = self.get_lca(stack[-1], v)
            
            # 维护单调栈，保持栈中节点在同一条树链上
            while len(stack) > 1 and self.dfn[lca] <= self.dfn[stack[-2]]:
                parent, child = stack[-2], stack.pop()
                self.vt[parent].append(child)
            
            if lca != stack[-1]:
                self.vt[lca] = []
                self.vt[lca].append(stack.pop())
                stack.append(lca)
            
            stack.append(v)
            
        # 栈中剩余节点连边
        for i in range(1, len(stack)):
            self.vt[stack[i-1]].append(stack[i])
            
        # 返回虚树真正的根（跳过哨兵 root）
        rt = root
        if self.is_critical[rt] != current_val and len(self.vt[rt]) == 1:
            rt = self.vt[rt][0]
        return rt

def interactionCosts(n: int, edges: list[list[int]], group: list[int]) -> int:
    adj = [[] for _ in range(n)]
    for v, w in edges:
        adj[v].append(w)
        adj[w].append(v)
        
    helper = VirtualTreeHelper(n, adj)
    
    # 按照权值分组
    nodes_map = {}
    for i, x in enumerate(group):
        nodes_map.setdefault(x, []).append(i)
        
    total_ans = 0

    for val, nodes in nodes_map.items():
        # 1. 构建虚树
        vt_root = helper.build_virtual_tree(nodes, val)
        
        # 2. 在虚树上通过 DFS 计算贡献
        num_nodes = len(nodes)
        
        def dfs(v):
            nonlocal total_ans
            # 只有标记为当前 val 的才是关键节点
            size = 1 if helper.is_critical[v] == val else 0
            for w in helper.vt[v]:
                sub_size = dfs(w)
                edge_weight = helper.dep[w] - helper.dep[v]
                # 贡献法：这条边被 (子树内点数 * 子树外点数) 对点跨越
                total_ans += edge_weight * sub_size * (num_nodes - sub_size)
                size += sub_size
            return size
            
        dfs(vt_root)
        
    return total_ans