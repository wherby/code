## UnionFind back 恢复的时候，需要把所有的路径一起恢复才有意义(因为路径压缩的时候更改了路径的关系)
# algorithm/codeforce/图论/二分图问题/二分图贪心划分.py

class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self._fa = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        # 路径压缩在这里是安全的，因为我们要么全删，要么全留
        if self._fa[x] != x:
            self._fa[x] = self.find(self._fa[x])
        return self._fa[x]

    def merge(self, from_: int, to: int) -> bool:
        x, y = self.find(from_), self.find(to)
        if x == y:
            return False
        # 按秩合并：将小树接到大树上
        if self.size[x] > self.size[y]:
            x, y = y, x
        self._fa[x] = y
        self.size[y] += self.size[x]
        return True

    def back(self, x: int):
        self._fa[x] = x
        self.size[x] = 1

    def init(self):
        """完全重置（O(N) 复杂度）"""
        for i in range(self.n):
            self._fa[i] = i
            self.size[i] = 1