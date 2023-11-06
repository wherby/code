## https://leetcode.cn/contest/weekly-contest-370/ranking/
## 雪景式

from testInput import *

from typing import List, Tuple, Optional

class SegmentTree():
    def __init__(self, init, unitX, f):
        self.f = f  # (X, X) -> X
        self.unitX = unitX
        self.f = f
        if type(init) == int:
            self.n = init
            self.n = 1 << (self.n - 1).bit_length()
            self.X = [unitX] * (self.n * 2)
        else:
            self.n = len(init)
            self.n = 1 << (self.n - 1).bit_length()
            # len(init)が2の累乗ではない時UnitXで埋める
            self.X = [unitX] * self.n + init + [unitX] * (self.n - len(init))
            # 配列のindex1まで埋める
            for i in range(self.n - 1, 0, -1):
                self.X[i] = self.f(self.X[i * 2], self.X[i * 2 | 1])

    def update(self, i, x):
        """0-indexedのi番目の値をxで置換"""
        # 最下段に移動
        i += self.n
        self.X[i] = self.f(self.X[i], x)
        # 上向に更新
        i >>= 1
        while i:
            self.X[i] = self.f(self.X[i * 2], self.X[i * 2 | 1])
            i >>= 1

    def getvalue(self, i):
        """元の配列のindexの値を見る"""
        return self.X[i + self.n]

    def getrange(self, l, r):
        """区間[l, r)でのfを行った値"""
        l += self.n
        r += self.n
        al = self.unitX
        ar = self.unitX
        while l < r:
            # 左端が右子ノードであれば
            if l & 1:
                al = self.f(al, self.X[l])
                l += 1
            # 右端が右子ノードであれば
            if r & 1:
                r -= 1
                ar = self.f(self.X[r], ar)
            l >>= 1
            r >>= 1
        return self.f(al, ar)

class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        n = len(nums)
        b = sorted(set([x - i for i, x in enumerate(nums)]))
        d = {x: i for i, x in enumerate(b)}
        tree = SegmentTree([-10**18] * (len(b) + 10), -10**18, max)
        for i in range(n):
            cur = nums[i] - i
            p = tree.getrange(0, d[cur] + 1)
            tree.update(d[cur], max(0,p) + nums[i])
        return tree.getrange(0, len(b) + 1)

import time

start = time.time()
re =Solution().maxBalancedSubsequenceSum(nums)
print(re)
end = time.time()
print(end - start)
