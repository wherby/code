class SparseTable:
    __slots__ = 'op', 'st'
    def __init__(self, nums, op):
        # op 需要满足可重复贡献，即 x op x = x，如 max, min, gcd, lcm, and, or
        # 建立 O(nlogn)，查询 O(1)
        n = len(nums)
        m = n.bit_length()
        st = [[0] * (n - (1<<b) + 1) for b in range(m)]
        for i, x in enumerate(nums):
            st[0][i] = x
        for b in range(1, m):
            l = 1 << (b-1)
            for i in range(n - (1<<b) + 1):
                st[b][i] = op(st[b-1][i], st[b-1][i+l])
        self.op = op
        self.st = st

    def query(self, left, right):
        b = (right - left + 1).bit_length() - 1
        return self.op(self.st[b][left], self.st[b][right - (1<<b) + 1])