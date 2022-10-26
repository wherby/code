# https://leetcode.cn/problems/count-subarrays-with-fixed-bounds/
# https://leetcode.cn/problems/count-subarrays-with-fixed-bounds/solution/by-freeyourmind-lexa/

from typing import List, Tuple, Optional
class SegmentTree():
    __slots__ = ['n', 'oper', 'e', 'log', 'size', 'data']

    def __init__(self, n, oper, e):
        self.n = n
        self.oper = oper
        self.e = e
        self.log = (n - 1).bit_length()
        self.size = 1 << self.log
        self.data = [e] * (2 * self.size)

    def _update(self, k):
        if self.oper:
            self.data[k] = self.data[2 * k] if self.data[2 * k] > self.data[2 * k + 1] else self.data[2 * k + 1]
        else:
            self.data[k] = self.data[2 * k] if self.data[2 * k] < self.data[2 * k + 1] else self.data[2 * k + 1]
        # self.data[k] = self.oper(self.data[2 * k], self.data[2 * k + 1])

    def build(self, arr):
        # assert len(arr) <= self.n
        for i in range(self.n):
            self.data[self.size + i] = arr[i]
        for i in range(self.size - 1, 0, -1):
            self._update(i)

    def set(self, p, x):
        # assert 0 <= p < self.n
        p += self.size
        self.data[p] = x
        for i in range(self.log):
            p >>= 1
            self._update(p)

    def get(self, p):
        # assert 0 <= p < self.n
        return self.data[p + self.size]

    def prod(self, l, r):
        # assert 0 <= l <= r <= self.n
        sml = smr = self.e
        l += self.size
        r += self.size
        while l < r:
            if l & 1:
                if self.oper:
                    sml = sml if sml > self.data[l] else self.data[l]
                else:
                    sml = sml if sml < self.data[l] else self.data[l]
                # sml = self.oper(sml, self.data[l])
                l += 1
            if r & 1:
                r -= 1
                if self.oper:
                    sml = sml if sml > self.data[r] else self.data[r]
                else:
                    sml = sml if sml < self.data[r] else self.data[r]
                # smr = self.oper(self.data[r], smr)
            l >>= 1
            r >>= 1
        if self.oper:
            return sml if sml > smr else smr
        else:
            return sml if sml < smr else smr
        # return self.oper(sml, smr)

    def all_prod(self):
        return self.data[1]

    def max_right(self, l, f):
        if l == self.n: return self.n
        l += self.size
        sm = self.e
        while True:
            while l % 2 == 0: l >>= 1
            if self.oper:
                tmp = f(sm if sm > self.data[l] else self.data[l])
            else:
                tmp = f(sm if sm < self.data[l] else self.data[l])
            if not tmp:
            # if not f(self.oper(sm, self.data[l])):
                while l < self.size:
                    l = 2 * l
                    if self.oper:
                        tmp = f(sm if sm > self.data[l] else self.data[l])
                    else:
                        tmp = f(sm if sm < self.data[l] else self.data[l])
                    if tmp:
                    # if f(self.oper(sm, self.data[l])):
                        if self.oper and sm < self.data[l] or not self.oper and sm > self.data[l]:
                            sm = self.data[l]

                    #     sm = self.oper(sm, self.data[l])
                        l += 1
                return l - self.size
            if self.oper and sm < self.data[l] or not self.oper and sm > self.data[l]:
                sm = self.data[l]
            # sm = self.oper(sm, self.data[l])
            l += 1
            if (l & -l) == l: break
        return self.n
    