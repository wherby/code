from testInput import *

from typing import List, Tuple, Optional

class Node(object): #线段树
    def __init__(self, lid = 0, rid = 0):
        self.val = 0
        self.delay = 0
        self.lid = lid
        self.rid = rid
        self.left = None
        self.right = None

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        self.base = 10 ** 9 + 7
        n = len(nums)
        left = {}
        root = self.build(0, n - 1)
        s2 = [0] * n
        for i, num in enumerate(nums):
            l = left.get(num, -1)
            s2[i] = (s2[i - 1] + self.query(root, l + 1, i) * 2 + i - l) % self.base
            self.update(root, l + 1, i, 1)
            left[num] = i
        return sum(s2) % self.base

    def build(self, l, r): #建立线段树
        if l == r:
            return Node(l, r)
        root = Node(l, r)
        m = (l + r) >> 1
        root.left = self.build(l, m)
        root.right = self.build(m + 1, r)
        return root

    def update(self, root, l1, r1, add):
        l = root.lid
        r = root.rid
        if r < l1 or l > r1: #当前区间和待更新区间无交集, 不处理
            pass
        elif l1 <= l and r <= r1: #当前区间包含于待更新区间, 懒操作
            root.val = (root.val + add * (r - l + 1)) % self.base #val包含delay部分
            root.delay = (root.delay + add) % self.base
        else:
            if root.delay != 0:
                self.update(root.left, root.left.lid, root.left.rid, root.delay)
                self.update(root.right, root.right.lid, root.right.rid, root.delay)
                root.delay = 0
            root.val = (self.update(root.left, l1, r1, add) + self.update(root.right, l1, r1, add)) % self.base
        return root.val

    def query(self, root, l1, r1):
        l = root.lid
        r = root.rid
        if r < l1 or l > r1: #当前区间和查询区间无交集
            return 0
        if l1 <= l and r <= r1: #当前区间包含于查询区间, 返回整个区间结果
            return root.val
        if root.delay != 0: #delay下放
            self.update(root.left, root.left.lid, root.left.rid, root.delay)
            self.update(root.right, root.right.lid, root.right.rid, root.delay)
            root.delay = 0
        return (self.query(root.left, l1, r1) + self.query(root.right, l1, r1)) % self.base
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        sum = [0] * (n * 4)
        todo = [0] * (n * 4)

        def do(o: int, l: int, r: int, add: int) -> None:
            sum[o] += add * (r - l + 1)
            todo[o] += add

        # o=1  [l,r] 1<=l<=r<=n
        # 把 [L,R] 加一，同时返回加一之前的区间和
        def query_and_add1(o: int, l: int, r: int, L: int, R: int) -> int:
            if L <= l and r <= R:
                res = sum[o]
                do(o, l, r, 1)
                return res

            m = (l + r) // 2
            add = todo[o]
            if add:
                do(o * 2, l, m, add)
                do(o * 2 + 1, m + 1, r, add)
                todo[o] = 0

            res = 0
            if L <= m: res += query_and_add1(o * 2, l, m, L, R)
            if m < R:  res += query_and_add1(o * 2 + 1, m + 1, r, L, R)
            sum[o] = sum[o * 2] + sum[o * 2 + 1]
            return res

        ans = s = 0
        last = {}
        for i, x in enumerate(nums, 1):
            j = last.get(x, 0)
            s += query_and_add1(1, 1, n, j + 1, i) * 2 + i - j
            ans += s
            last[x] = i
        return ans % 1_000_000_007


import time

start = time.time()
re =Solution().sumCounts(nums)
print(re)
end = time.time()
print(end - start)