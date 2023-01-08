# https://leetcode.cn/problems/coin-bonus/
# Using dfs order  to record node and child node relationship


M = int(1e9 + 7)

class BIT:
    def __init__(self, n):
        self.n = n + 5
        self.sum = [0 for _ in range(n + 10)]
        self.ntimessum = [0 for _ in range(n + 10)]
    
    def lowbit(self, x):
        return x & (-x)

    # 在 pos 位置加上 k
    def update(self, pos, k):
        x = pos
        while pos <= self.n:
            self.sum[pos] += k
            self.sum[pos] %= M
            self.ntimessum[pos] += k * (x - 1)
            self.ntimessum[pos] %= M
            pos += self.lowbit(pos)
    
    # 区间更新 + 单点查询
    def askis(self, pos):
        if not pos:
            return 0
        ret = 0
        while pos:
            ret += self.sum[pos]
            ret %= M
            pos -= lowbit(pos)
        return ret
    
    # 单点更新 + 区间查询
    def asksi(self, l, r):
        if l > r:
            return 0
        return askis(r) - askis(l - 1)
    
    # 单点更新 + 单点查询
    def askss(self, pos):
        return askis(pos) - askis(pos - 1)
    
    # 区间更新 + 区间查询
    def askii(self, pos):
        if not pos:
            return 0
        ret = 0
        x = pos
        while pos:
            ret += x * self.sum[pos] - self.ntimessum[pos]
            ret %= M
            pos -= self.lowbit(pos)
        return ret

class Solution:
    def bonus(self, n: int, leadership: List[List[int]], operations: List[List[int]]) -> List[int]:
        
        # 邻接表
        g = [[] for _ in range(n + 1)]
        begin = [0 for _ in range(n + 1)]
        end = [0 for _ in range(n + 1)]
        id = 1

        for l in leadership:
            g[l[0]].append(l[1])
        
        # 深搜
        def dfs(cur):
            nonlocal id
            begin[cur] = id
            for child in g[cur]:
                dfs(child)
            end[cur] = id
            id += 1
        dfs(1)
        
        # 树状数组
        b = BIT(n)
        ret = []
        for q in operations:
            if q[0] == 1:
                b.update(end[q[1]], q[2])
                b.update(end[q[1]] + 1, -q[2])
            elif q[0] == 2:
                b.update(begin[q[1]], q[2])
                b.update(end[q[1]] + 1, -q[2])
            else:
                ans = b.askii(end[q[1]]) - b.askii(begin[q[1]] - 1)
                ret.append((ans % M + M) % M)

        return ret

# 作者：BNDSllx
# 链接：https://leetcode.cn/problems/coin-bonus/solution/xiao-ai-lao-shi-li-kou-bei-li-jie-zhen-t-rut3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。