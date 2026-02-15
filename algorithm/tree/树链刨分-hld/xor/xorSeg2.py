# https://leetcode.cn/problems/palindromic-path-queries-in-a-tree/solutions/3902929/liang-chong-fang-fa-si-fen-mo-ban-da-fan-8u4d/

# 重链剖分
class HeavyLightDecompositon:
    __slots__ = 'parent', 'depth', 'size', 'hson', 'order', 'dfn', 'top'
    def __init__(self, g, rt=0):
        n = len(g)
        self.parent = parent = [-1] * n
        self.depth = depth = [0] * n
        self.size = size = [1] * n
        self.hson = hson = [-1] * n
        self.order = order = [0] * n
        self.dfn = dfn = [0] * n
        self.top = top = [0] * n
        stk = [rt]
        time = 0
        # 第一次 DFS
        while stk:
            u = stk.pop()
            order[time] = u
            time += 1
            for v in g[u]:
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    stk.append(v)
        for u in reversed(order):
            mxsz = 0
            for v in g[u]:
                if v != parent[u]:
                    if size[v] > mxsz:
                        mxsz = size[v]
                        hson[u] = v
                    size[u] += size[v]
        stk.append(rt)
        time = 0
        top[rt] = rt
        # 第二次 DFS
        while stk:
            u = stk.pop()
            order[time] = u
            dfn[u] = time
            time += 1
            for v in g[u]:
                if v != parent[u] and v != hson[u]:
                    top[v] = v
                    stk.append(v)
            if hson[u] != -1:
                top[hson[u]] = top[u]
                stk.append(hson[u])

    def kth_ancestor(self, u, k):
        depth = self.depth
        top = self.top
        assert 0 <= k <= depth[u]
        d = depth[u] - k
        while depth[u] >= d:
            tu = top[u]
            if depth[tu] <= d:
                return self.order[self.dfn[tu] + d - depth[tu]]
            u = self.parent[tu]

    def get_lca(self, u, v):
        depth = self.depth
        top = self.top
        parent = self.parent
        while top[u] != top[v]:
            if depth[top[u]] < depth[top[v]]:
                u, v = v, u
            u = parent[top[u]]
        return u if depth[u] < depth[v] else v

    def get_path(self, u, v):
        # 生成 u-v 的路径上经过的链
        # 注意：链按顺序排列，但链上从 u 到 lca 的节点不按顺序排列
        pathu, pathv = [], []
        depth = self.depth
        top = self.top
        dfn = self.dfn
        parent = self.parent
        while (tu := top[u]) != (tv := top[v]):
            # DFS order 上区间的左右端点，闭区间
            if depth[tu] >= depth[tv]:
                pathu.append((dfn[tu], dfn[u]))
                u = parent[tu]
            else:
                pathv.append((dfn[tv], dfn[v]))
                v = parent[tv]

        pathu.append((dfn[u], dfn[v]) if depth[u] < depth[v] else ((dfn[v], dfn[u])))
        pathv.reverse()
        return pathu + pathv

# 线段树
class SegmentTree:
    __slots__ = 'n', 'height', 'size', 'idval', 'op', 'tree'
    def __init__(self, nums, idval=0, op=int.__add__):
        self.n = len(nums)
        self.height = (self.n-1).bit_length()
        self.size = 1 << self.height
        self.idval = idval
        self.op = op

        self.tree = [idval for _ in range(2 * self.size)]
        self.tree[self.size:self.size+self.n] = nums
        for idx in range(self.size-1, 0, -1):
            self.pushup(idx)

    def pushup(self, rt):
        self.tree[rt] = self.op(self.tree[rt*2], self.tree[rt*2+1])

    def update(self, idx, val):
        idx += self.size
        self.tree[idx] = val
        for i in range(1, self.height + 1):
            self.pushup(idx >> i)

    def query(self, left, right):
        # 闭区间 [left, right]
        left += self.size
        right += self.size

        lres, rres = self.idval, self.idval
        while left <= right:
            if left & 1:
                lres = self.op(lres, self.tree[left])
                left += 1
            if not right & 1:
                rres = self.op(self.tree[right], rres)
                right -= 1
            left >>= 1
            right >>= 1

        return self.op(lres, rres)

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        hld = HeavyLightDecompositon(g)
        dfn = hld.dfn
        s = [1 << (ord(ch) - 97) for ch in s]
        order = [s[u] for u in hld.order]
        seg = SegmentTree(order, 0, int.__xor__)

        ans = []
        for q in queries:
            tp, u, v = q.split()
            if tp[0] == 'q':
                u = int(u); v = int(v)
                res = 0
                for l, r in hld.get_path(u, v):
                    res ^= seg.query(l, r)
                ans.append(res & (res - 1) == 0)
            else:
                u = int(u); v = 1 << (ord(v) - 97)
                seg.update(dfn[u], v)

        return ans



# 作者：FatalError
# 链接：https://leetcode.cn/problems/palindromic-path-queries-in-a-tree/solutions/3902929/liang-chong-fang-fa-si-fen-mo-ban-da-fan-8u4d/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。