
# https://leetcode.cn/problems/subarrays-distinct-element-sum-of-squares-i/description/?envType=daily-question&envId=2026-10-15
# 给你一个下标从 0 开始的整数数组 nums 。
# 定义 nums 一个子数组的 不同计数 值如下：
# 令 nums[i..j] 表示 nums 中所有下标在 i 到 j 范围内的元素构成的子数组（满足 0 <= i <= j < nums.length ），那么我们称子数组 nums[i..j] 中不同值的数目为 nums[i..j] 的不同计数。
# 请你返回 nums 中所有子数组的 不同计数 的 平方 和。
# 子数组指的是一个数组里面一段连续 非空 的元素序列。

# algorithm/segmentTree/docs/子数组贡献法线段树.md


from typing import List

class LazySegmentTree:
    """
    Reference
    https://github.com/atcoder/ac-library/blob/master/atcoder/lazysegtree.hpp
    https://github.com/atcoder/ac-library/blob/master/document_en/lazysegtree.md
    https://github.com/atcoder/ac-library/blob/master/document_ja/lazysegtree.md
    """
    def __init__(self, n, op, e, mapping, composition, id):
        self.n = n
        self.op = op
        self.e = e
        self.mapping = mapping
        self.composition = composition
        self.id = id
        self.log = (n - 1).bit_length()
        self.size = 1 << self.log
        self.d = [e] * (2 * self.size)
        self.lz = [id] * (self.size)

    def update(self, k):
        self.d[k] = self.op(self.d[2 * k], self.d[2 * k + 1])

    def all_apply(self, k, f):
        self.d[k] = self.mapping(f, self.d[k])
        if k < self.size:
            self.lz[k] = self.composition(f, self.lz[k])

    def push(self, k):
        if self.lz[k] != self.id:
            self.all_apply(2 * k, self.lz[k])
            self.all_apply(2 * k + 1, self.lz[k])
            self.lz[k] = self.id

    def build(self, v):
        assert len(v) <= self.n
        for i in range(len(v)):
            self.d[self.size + i] = v[i]
        for i in range(self.size - 1, 0 ,-1):
            self.update(i)

    def set(self, p, x):
        assert 0 <= p < self.n
        p += self.size
        for i in range(self.log, 0, -1):
            self.push(p >> i)
        self.d[p] = x
        for i in range(1, self.log + 1):
            self.update(p >> i)

    def get(self, p):
        assert 0 <= p < self.n
        p += self.size
        for i in range(self.log, 0, -1):
            self.push(p >> i)
        return self.d[p]

    def prod(self, l, r):
        assert 0 <= l <= r <= self.n
        if l == r:
            return self.e
        l += self.size
        r += self.size
        for i in range(self.log, 0, -1):
            if (l >> i) << i != l:
                self.push(l >> i)
            if (r >> i) << i != r:
                self.push((r-1) >> i)
        sml = smr = self.e
        while l < r:
            if l & 1:
                sml = self.op(sml, self.d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self.op(self.d[r], smr)
            l >>= 1
            r >>= 1
        return self.op(sml, smr)

    def all_prod(self):
        return self.d[1]

    # def apply(self, p, f):
    #     assert 0 <= p < self.n
    #     p += self.size
    #     for i in range(self.log, 0, -1):
    #         self.push(p >> i)
    #     self.d[p] = self.mapping(f, self.d[p])
    #     for i in range(1, self.log + 1):
    #         self.update(p >> i)
    
    # (2) It applies a[i] = f(a[i]) for all i = l..r-1.
    # 跟新的是前闭后开区间 [l,r)
    def apply(self, l, r, f):
        assert 0 <= l <= r <= self.n
        if l == r:
            return
        l += self.size
        r += self.size
        for i in range(self.log, 0, -1):
            if (l >> i) << i != l:
                self.push(l >> i)
            if (r >> i) << i != r:
                self.push((r - 1) >> i)
        l2 = l
        r2 = r
        while l < r:
            if l & 1:
                self.all_apply(l, f)
                l += 1
            if r & 1:
                r -= 1
                self.all_apply(r, f)
            l >>= 1
            r >>= 1
        l = l2
        r = r2
        for i in range(1, self.log + 1):
            if (l >> i) << i != l:
                self.update(l >> i)
            if (r >> i) << i != r:
                self.update((r - 1) >> i)

    # maxright: 从l 开始向右查询，找到第一个不符合g的
    def max_right(self, l, g):
        assert 0 <= l <= self.n
        assert g(self.e)
        #print(g,self.e)
        if l == self.n:
            return self.n
        l += self.size
        for i in range(self.log, 0, -1):
            self.push(l >> i)
        sm = self.e
        while True:
            while l % 2 == 0:
                l >>= 1
            #print(l,self.d[l],self.op(sm, self.d[l]))
            if not g(self.op(sm, self.d[l])):
                while l < self.size:
                    self.push(l)
                    l = 2 * l
                    if g(self.op(sm, self.d[l])):
                        sm = self.op(sm, self.d[l])
                        l += 1
                #print(sm)
                return l - self.size
            sm = self.op(sm, self.d[l])
            l += 1
            if (l & -l) == l:
                return self.n

    # 从r开始往左查询。查找最小符合g的l
    def min_left(self, r, g):
        assert 0 <= r <= self.n
        assert g(self.e)
        if r == 0:
            return 0
        r += self.size
        for i in range(self.log, 0, -1):
            self.push((r - 1) >> i)
        sm = self.e
        while True:
            r -= 1
            while r > 1 and r % 2:
                r >>= 1
            if not g(self.op(self.d[r], sm)):
                while r < self.size:
                    self.push(r)
                    r = 2 * r + 1
                    if g(self.op(self.d[r], sm)):
                        sm = self.op(self.d[r], sm)
                        r -= 1
                return r + 1 - self.size
            sm = self.op(self.d[r], sm)
            #print(sm,"sm",self.d[r],r)
            if (r & -r) == r:
                return 0



class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 1_000_000_007

        # 定义 LazySegmentTree 的代数结构
        op = lambda a, b: (a[0] + b[0], a[1] + b[1])
        e = (0, 0)
        mapping = lambda f, x: (x[0] + f * x[1], x[1])
        composition = lambda f, g: f + g
        id_f = 0

        # 初始化 LazySegmentTree
        seg = LazySegmentTree(n, op, e, mapping, composition, id_f)

        # 构建初始数组：每个位置的初始值为 (0, 1)，即 sum_val=0, size=1
        init_val = [(0, 1)] * n
        seg.build(init_val)

        ans = 0
        s = 0
        last = {}

        for i, x in enumerate(nums):
            # 找到 x 上一次出现的下标，若没有出现过则为 -1
            j = last.get(x, -1)

            # 1. 区间查询：查询前闭后开区间 [j + 1, i + 1) 内的元素和 s1
            # prod(l, r) 对应区间 [l, r)
            s1 = seg.prod(j + 1, i + 1)[0]

            # 2. 区间更新：将前闭后开区间 [j + 1, i + 1) 内的所有元素加 1
            # apply(l, r, f) 对应区间 [l, r)
            seg.apply(j + 1, i + 1, 1)

            # 3. 根据公式更新右端点为 i 时的平方和 s
            s += 2 * s1 + (i - j)

            # 4. 累加到总答案
            ans += s

            # 5. 更新 x 的最近出现位置
            last[x] = i

        return ans % MOD
    

re = Solution().sumCounts( [1,2,1])
print(re)