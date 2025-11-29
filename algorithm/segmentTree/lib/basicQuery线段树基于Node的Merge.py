# https://leetcode.com/contest/weekly-contest-477/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/description/
from typing import List, Tuple, Optional
MOD = 10**9 + 7

def mod_pow(a, b, mod):
    result = 1
    while b:
        if b & 1:
            result = result * a % mod
        a = a * a % mod
        b >>= 1
    return result

class SegmentNode:
    __slots__ = ('val', 'sum', 'cnt')
    def __init__(self, val=0, sum_val=0, cnt=0):
        self.val = val      # 拼接值 mod MOD
        self.sum = sum_val  # 数字和
        self.cnt = cnt      # 非零数字个数

class SegmentTree:
    def __init__(self, s):
        self.n = len(s)
        self.s = s
        self.size = 1
        while self.size < self.n:
            self.size <<= 1
        self.tree = [SegmentNode() for _ in range(2 * self.size)]
        self.build(s)
    
    def build(self, s):
        # 构建叶子节点
        for i in range(self.n):
            digit = int(s[i])
            node = SegmentNode()
            if digit != 0:
                node.val = digit % MOD
                node.sum = digit
                node.cnt = 1
            self.tree[self.size + i] = node
        
        # 构建内部节点
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.merge(self.tree[2*i], self.tree[2*i+1])
    
    def merge(self, left, right):
        if left.cnt == 0:
            return right
        if right.cnt == 0:
            return left
            
        # 关键合并逻辑
        pow_val = mod_pow(10, right.cnt, MOD)
        new_val = (left.val * pow_val + right.val) % MOD
        new_sum = left.sum + right.sum
        new_cnt = left.cnt + right.cnt
        
        return SegmentNode(new_val, new_sum, new_cnt)
    
    def query(self, l, r):
        # 查询区间 [l, r]
        l += self.size
        r += self.size
        left_res = SegmentNode()
        right_res = SegmentNode()
        
        while l <= r:
            if l % 2 == 1:
                left_res = self.merge(left_res, self.tree[l])
                l += 1
            if r % 2 == 0:
                right_res = self.merge(self.tree[r], right_res)
                r -= 1
            l //= 2
            r //= 2
        
        return self.merge(left_res, right_res)

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        seg_tree = SegmentTree(s)
        results = []
        
        for l, r in queries:
            node = seg_tree.query(l, r)
            if node.cnt == 0:
                results.append(0)
            else:
                results.append(node.val * node.sum % MOD)
        
        return results