import sys

# 提高读取速度
input = sys.stdin.readline

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
    
        tin, tout = [0] * n, [0] * n
        depth = [0] * n
        timer = 0
        LOG = 18
        up = [[-1] * LOG for _ in range(n)]
        
        # --- 迭代 DFS 代替递归 ---
        # stack 存储 (当前节点, 父节点)
        stack = [(0, -1)]
        while stack:
            u, p = stack.pop()
            if u >= 0:  # 第一次访问（入戳）
                tin[u] = timer
                timer += 1
                up[u][0] = p
                
                # 预处理倍增表
                for i in range(1, LOG):
                    if up[u][i-1] != -1:
                        up[u][i] = up[up[u][i-1]][i-1]
                    else:
                        break
                
                # 标记回溯并压入子节点
                stack.append((~u, p))
                for v in adj[u]:
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u))
            else:  # 回溯（出戳）
                u = ~u
                tout[u] = timer - 1

        # --- 辅助函数：LCA ---
        def get_lca(u, v):
            if depth[u] < depth[v]: u, v = v, u
            # 先跳到同一深度
            diff = depth[u] - depth[v]
            for i in range(LOG):
                if (diff >> i) & 1:
                    u = up[u][i]
            if u == v: return u
            # 同步向上跳
            for i in range(LOG - 1, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
            return up[u][0]

        # --- 差分 BIT 实现区间异或 ---
        bit = [0] * (n + 1)
        def update_bit(idx, val):
            idx += 1 # BIT 索引从 1 开始
            while idx <= n:
                bit[idx] ^= val
                idx += idx & (-idx)

        def query_bit(idx):
            idx += 1
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res

        # --- 初始化 BIT ---
        ms = [1 << (ord(c) - 97) for c in s]
        for i in range(n):
            # 差分更新：[tin[i], tout[i]] 区间异或 ms[i]
            update_bit(tin[i], ms[i])
            update_bit(tout[i] + 1, ms[i])
    
        ans = []
        for q in queries:
            p = q.split()
            if p[0] == "update":
                u, char = int(p[1]), p[2]
                nm = 1 << (ord(char) - 97)
                diff = ms[u] ^ nm
                # 同样的区间差分逻辑
                update_bit(tin[u], diff)
                update_bit(tout[u] + 1, diff)
                ms[u] = nm
            else:
                u, v = int(p[1]), int(p[2])
                lca = get_lca(u, v)
                # 核心公式：PathXOR = dist(u) ^ dist(v) ^ char(LCA)
                px = query_bit(tin[u]) ^ query_bit(tin[v]) ^ ms[lca]
                # 回文判定：奇数次出现的字符不超过 1 个
                ans.append((px & (px - 1)) == 0)
        print(tin, tout)
        return ans

re = Solution().palindromePath(n = 4, edges = [[0,1],[0,2],[0,3]], s = "abca", queries = ["query 1 2","update 0 b","query 2 3","update 3 a","query 1 3"])
print(re)