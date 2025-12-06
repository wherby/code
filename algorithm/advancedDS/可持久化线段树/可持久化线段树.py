# https://leetcode.cn/contest/weekly-contest-478/ranking/?region=local_v2  # 细菌小子

import bisect
from typing import List


class TreeNode:
    __slots__ = ['left', 'right', 'cnt', 'sum']

    def __init__(self):
        self.left = None
        self.right = None
        self.cnt = 0
        self.sum = 0


class SparseTable:
    def __init__(self, arr):
        n = len(arr)
        self.n = n
        logn = n.bit_length()
        self.min_dp = [[0] * n for _ in range(logn)]
        self.max_dp = [[0] * n for _ in range(logn)]
        self.min_dp[0] = arr[:]
        self.max_dp[0] = arr[:]
        for j in range(1, logn):
            step = 1 << (j - 1)
            for i in range(n - (1 << j) + 1):
                self.min_dp[j][i] = min(self.min_dp[j - 1][i], self.min_dp[j - 1][i + step])
                self.max_dp[j][i] = max(self.max_dp[j - 1][i], self.max_dp[j - 1][i + step])

    def query_min(self, l, r):
        length = r - l + 1
        j = length.bit_length() - 1
        return min(self.min_dp[j][l], self.min_dp[j][r - (1 << j) + 1])

    def query_max(self, l, r):
        length = r - l + 1
        j = length.bit_length() - 1
        return max(self.max_dp[j][l], self.max_dp[j][r - (1 << j) + 1])


class PersistentSegmentTree:
    def __init__(self, n, size, vals):
        self.size = size
        self.vals = vals
        self.roots = [None] * (n + 1)
        self.roots[0] = self._build(0, size - 1)

    def _build(self, l, r):
        node = TreeNode()
        if l == r:
            return node
        mid = (l + r) // 2
        node.left = self._build(l, mid)
        node.right = self._build(mid + 1, r)
        return node

    def update(self, pre_node, l, r, pos, val):
        node = TreeNode()
        node.cnt = pre_node.cnt + 1
        node.sum = pre_node.sum + val
        if l == r:
            return node
        mid = (l + r) // 2
        if pos <= mid:
            node.left = self.update(pre_node.left, l, mid, pos, val)
            node.right = pre_node.right
        else:
            node.left = pre_node.left
            node.right = self.update(pre_node.right, mid + 1, r, pos, val)
        return node

    def query_kth(self, node1, node2, l, r, k):
        if l == r:
            return l
        mid = (l + r) // 2
        left_cnt = node2.left.cnt - node1.left.cnt
        if left_cnt >= k:
            return self.query_kth(node1.left, node2.left, l, mid, k)
        else:
            return self.query_kth(node1.right, node2.right, mid + 1, r, k - left_cnt)

    def query_range(self, node1, node2, l, r, ql, qr):
        if ql <= l and r <= qr:
            return node2.cnt - node1.cnt, node2.sum - node1.sum
        mid = (l + r) // 2
        cnt_total, sum_total = 0, 0
        if ql <= mid:
            cnt_left, sum_left = self.query_range(node1.left, node2.left, l, mid, ql, qr)
            cnt_total += cnt_left
            sum_total += sum_left
        if qr > mid:
            cnt_right, sum_right = self.query_range(node1.right, node2.right, mid + 1, r, ql, qr)
            cnt_total += cnt_right
            sum_total += sum_right
        return cnt_total, sum_total


class Solution:
    def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        rem = [x % k for x in nums]
        b = [(nums[i] - rem[i]) // k for i in range(n)]

        vals = sorted(set(b))
        size = len(vals)
        idx_b = [0] * n
        for i in range(n):
            idx_b[i] = bisect.bisect_left(vals, b[i])

        st = SparseTable(rem)

        pst = PersistentSegmentTree(n, size, vals)
        for i in range(n):
            pst.roots[i + 1] = pst.update(pst.roots[i], 0, size - 1, idx_b[i], b[i])

        ans = []
        for li, ri in queries:
            min_r = st.query_min(li, ri)
            max_r = st.query_max(li, ri)
            if min_r != max_r:
                ans.append(-1)
            else:
                L = ri - li + 1
                kth = (L + 1) // 2
                pos = pst.query_kth(pst.roots[li], pst.roots[ri + 1], 0, size - 1, kth)
                m = vals[pos]
                cnt_left, sum_left = pst.query_range(pst.roots[li], pst.roots[ri + 1], 0, size - 1, 0, pos)
                total_cnt, total_sum = pst.query_range(pst.roots[li], pst.roots[ri + 1], 0, size - 1, 0, size - 1)
                cnt_right = L - cnt_left
                total_right = total_sum - sum_left
                operations = (m * cnt_left - sum_left) + (total_right - m * cnt_right)
                ans.append(operations)
        return ans