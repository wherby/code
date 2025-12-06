# https://leetcode.cn/contest/weekly-contest-478/ranking/?region=local_v2  # pku_erutan

from typing import List, Tuple, Optional
class TreeNode:
    __slots__ = ('left', 'right', 'cnt', 'sum')
    def __init__(self):
        self.left = None
        self.right = None
        self.cnt = 0
        self.sum = 0

class PersistentSegmentTree:
    def __init__(self, values):
        self.vals = sorted(set(values))
        self.size = len(self.vals)
        self.roots = [self.build(0, self.size-1)]
        
        # 构建映射
        self.mapping = {}
        for idx, val in enumerate(self.vals):
            self.mapping[val] = idx
    
    def build(self, l, r):
        node = TreeNode()
        if l == r:
            return node
        mid = (l + r) // 2
        node.left = self.build(l, mid)
        node.right = self.build(mid+1, r)
        return node

    def update(self, pre_node, l, r, idx, val):
        node = TreeNode()
        node.cnt = pre_node.cnt + 1
        node.sum = pre_node.sum + val
        if l == r:
            return node
        
        mid = (l + r) // 2
        if idx <= mid:
            node.left = self.update(pre_node.left, l, mid, idx, val)
            node.right = pre_node.right
        else:
            node.left = pre_node.left
            node.right = self.update(pre_node.right, mid+1, r, idx, val)
        return node

    def query_kth(self, node1, node2, l, r, k):
        if l == r:
            return self.vals[l], self.vals[l] * k
        
        mid = (l + r) // 2
        left_cnt = node2.left.cnt - node1.left.cnt
        left_sum = node2.left.sum - node1.left.sum
        
        if k <= left_cnt:
            return self.query_kth(node1.left, node2.left, l, mid, k)
        else:
            val, right_sum = self.query_kth(node1.right, node2.right, mid+1, r, k - left_cnt)
            return val, left_sum + right_sum

    def query_range(self, l_idx, r_idx, k):
        if l_idx < 0 or r_idx >= len(self.roots)-1 or l_idx > r_idx:
            return 0, 0
        root1 = self.roots[l_idx]
        root2 = self.roots[r_idx+1]
        return self.query_kth(root1, root2, 0, self.size-1, k)

class Solution:
    def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        ise = []
        for i in range(n-1) :
            ise.append(1 if (nums[i+1]-nums[i])%k>0 else 0)
        presum_ise = [0]
        for t in ise :
            presum_ise.append(presum_ise[-1]+t)


        pre_sum = [0]
        for t in nums :
            pre_sum.append(pre_sum[-1]+t)
            
        pst = PersistentSegmentTree(nums)
        for num in nums:
            idx = pst.mapping[num]
            new_root = pst.update(pst.roots[-1], 0, pst.size-1, idx, num)
            pst.roots.append(new_root)

        to_ret = []
        for l, r in queries :
            nt = presum_ise[r] - presum_ise[l]
            if not nt == 0 :
                to_ret.append(-1)
                continue

            L = r - l + 1
            mid_index = (L + 1) // 2
            median, left_sum = pst.query_range(l, r, mid_index)
            total = pre_sum[r+1] - pre_sum[l]
            operations = (median * mid_index - left_sum) + (total - left_sum - median * (L - mid_index))
            to_ret.append(operations//k)

        return to_ret
            

        
            

            