

class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def lowbit(self, i):
        return i & (-i)

    def update(self, i, delta):
        """将第 i 个元素增加 delta (i 从 1 开始)"""
        while i <= self.size:
            self.tree[i] += delta
            i += self.lowbit(i)

    def query(self, i):
        """查询前 i 个元素的和 (i 从 1 开始)"""
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= self.lowbit(i)
        return res