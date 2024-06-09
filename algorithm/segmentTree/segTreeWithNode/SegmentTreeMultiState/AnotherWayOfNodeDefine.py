# https://leetcode-cn.com/contest/weekly-contest-285/problems/longest-substring-of-one-repeating-character/
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
            # len(init)が2の累乗ではない时UnitXで埋める
            self.X = [unitX] * self.n + init + [unitX] * (self.n - len(init))
            # 配列のindex1まで埋める
            for i in range(self.n - 1, 0, -1):
                self.X[i] = self.f(self.X[i * 2], self.X[i * 2 | 1])

    def update(self, i, x):
        """0-indexedのi番目の値をxで置换"""
        # 最下段に移动
        i += self.n
        self.X[i] = x
        # 上向に更新
        i >>= 1
        while i:
            self.X[i] = self.f(self.X[i * 2], self.X[i * 2 | 1])
            i >>= 1

    def getvalue(self, i):
        """元の配列のindexの値を见る"""
        return self.X[i + self.n]

    def getrange(self, l, r):
        """区间[l, r)でのfを行った値"""
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


def op(x, y):
    # 仅包含第一个数，仅包含最后一个数，不包含第一个数和最后一个数，既包含第一个数又包含最后一个数
    a1, b1, c1, d1 = x
    a2, b2, c2, d2 = y
    return max(a1 + max(a2,c2),d1 + c2), max(b1 + b2, c1 + max(b2,d2)), max(b1 + c2, c1 + max(a2,c2)), max(a1 + max(d2, b2), d1 + b2)


class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        Mod = 10 ** 9 + 7
        n = len(nums)
        tree = SegmentTree([[0, 0, 0, max(0, nums[i])] for i in range(n)], [0] * 4, op)
        ans = 0
        for i, x in queries:
            tree.update(i, [0, 0, 0, max(0, x)])
            ans += max(tree.getrange(0, n))
            ans %= Mod
        return ans

#作者：雪景式
#链接：https://leetcode.cn/circle/discuss/62U280/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。