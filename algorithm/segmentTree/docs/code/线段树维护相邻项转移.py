class SegmentTree:
    __slots__ = ['n', 'oper', 'e', 'log', 'size', 'data']

    def __init__(self, n, oper, e):
        self.n = n
        self.oper = oper
        self.e = e
        self.log = (n - 1).bit_length()
        self.size = 1 << self.log
        self.data = [e] * (2 * self.size)

    def _update(self, k):
        self.data[k] = self.oper(self.data[2 * k], self.data[2 * k + 1])

    def build(self, arr):
        self.data[self.size:self.size + self.n] = arr
        for i in range(self.size - 1, 0, -1):
            self._update(i)

    def set(self, p, x):
        p += self.size
        self.data[p] = x
        for _ in range(self.log):
            p >>= 1
            self._update(p)

    def get(self, p):
        return self.data[p + self.size]

    def prod(self, l, r):
        sml = smr = self.e
        l += self.size
        r += self.size
        while l < r:
            if l & 1:
                sml = self.oper(sml, self.data[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self.oper(self.data[r], smr)
            l >>= 1
            r >>= 1
        return self.oper(sml, smr)

    def all_prod(self):
        return self.data[1]

    def max_right(self, l, f):
        if l == self.n:
            return self.n
        l += self.size
        sm = self.e
        while True:
            while l % 2 == 0:
                l >>= 1
            if not f(self.oper(sm, self.data[l])):
                while l < self.size:
                    l *= 2
                    if f(self.oper(sm, self.data[l])):
                        sm = self.oper(sm, self.data[l])
                        l += 1
                return l - self.size
            sm = self.oper(sm, self.data[l])
            l += 1
            if (l & -l) == l:
                break
        return self.n

    def min_left(self, r, f):
        if r == 0:
            return 0
        r += self.size
        sm = self.e
        while True:
            r -= 1
            while r > 1 and r & 1:
                r >>= 1
            if not f(self.oper(self.data[r], sm)):
                while r < self.size:
                    r = 2 * r + 1
                    if f(self.oper(self.data[r], sm)):
                        sm = self.oper(self.data[r], sm)
                        r -= 1
                return r + 1 - self.size
            sm = self.oper(self.data[r], sm)
            if (r & -r) == r:
                break
        return 0


E = (-1, -1, 0)

def merge(a, b):
    if a[0] < 0:
        return b
    if b[0] < 0:
        return a
    return a[0], b[1], a[2] + b[2] - a[1] * b[0]


class Solution:
    def countOfPeaks(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)

        def node(i):
            return (i, i, i * i) if nums[i - 1] < nums[i] > nums[i + 1] else E

        st = SegmentTree(n, merge, E)
        st.build([E] + [node(i) for i in range(1, n - 1)] + [E])

        res = []

        for op, x, y in queries:
            if op == 1:
                p, q, v = st.prod(x + 1, y)
                res.append(0 if p < 0 else y * (q - x) + p * x - v)
                continue

            nums[x] = y
            for i in range(max(1, x - 1), min(n - 1, x + 2)):
                v = node(i)
                if st.get(i) != v:
                    st.set(i, v)

        return res