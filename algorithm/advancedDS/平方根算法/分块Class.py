# https://leetcode.cn/contest/weekly-contest-503/problems/number-of-pairs-after-increment/description/
from typing import List, Tuple, Optional
from collections import Counter
class RangeAddFreq:
    def __init__(self, A, S=346):
        self.A = A
        self.S = S
        self.n = len(A)
        self.m = (self.n + S - 1) // S
        self.cnt = [Counter(A[i * S:(i + 1) * S]) for i in range(self.m)]
        self.tag = [0] * self.m

    def rebuild(self, b):
        S = self.S
        self.cnt[b] = Counter(self.A[b * S:min(self.n, (b + 1) * S)])

    def add_part(self, l, r, v):
        A = self.A
        for i in range(l, r + 1):
            A[i] += v
        self.rebuild(l // self.S)

    def add(self, l, r, v):
        S = self.S
        bl, br = l // S, r // S
        if bl == br:
            self.add_part(l, r, v)
        else:
            self.add_part(l, (bl + 1) * S - 1, v)
            self.add_part(br * S, r, v)
            for b in range(bl + 1, br):
                self.tag[b] += v

    def count(self, x):
        return sum(c[x - t] for c, t in zip(self.cnt, self.tag))

    def get(self, i):
        return self.A[i] + self.tag[i // self.S]

class Solution:
    def numberOfPairs(self, A: List[int], B: List[int], Q: List[List[int]]) -> List[int]:
        s = RangeAddFreq(B)

        res = []
        P = list(Counter(A).items())

        for q in Q:
            match q:
                case [1, l, r, v]:
                    s.add(l, r, v)
                case [2, t]:
                    res.append(sum(c * s.count(t - a) for a, c in P))

        return res