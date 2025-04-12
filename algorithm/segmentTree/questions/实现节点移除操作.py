# https://leetcode.cn/problems/minimum-pair-removal-to-sort-array-ii/solutions/3643034/chun-xian-duan-shu-by-ling-jian-2012-bu47/
# 节点移除就是把节点指向重复节点，实现树的更新
from typing import List, Tuple, Optional
from math import inf


class SegTree:
    def __init__(self, left, right, single_value=None):
        if left is None and right is None:
            assert single_value is not None
            self.min_pair = inf
            self.nondec = True
            self.left_most_value = single_value
            self.right_most_value = single_value
            self.left = self.right = None
        else:
            self.left = left
            self.right = right
            self._update_info()

    def _update_info(self):
        self.left_most_value = self.left.left_most_value
        self.right_most_value = self.right.right_most_value
        self.min_pair = min(self.left.min_pair, self.right.min_pair, self.left.right_most_value + self.right.left_most_value)
        self.nondec = self.left.nondec and self.right.nondec and self.left.right_most_value <= self.right.left_most_value

    def add_right(self, value):
        if self.right is None:
            self.left_most_value += value
            self.right_most_value += value
        else:
            self.right.add_right(value)
            self._update_info()

    def remove_left(self):
        if self.left is None:
            return None
        else:
            left = self.left.remove_left()
            if left is None:
                return self.right
            else:
                self.left = left
                self._update_info()
                return self

    def merge_min(self):
        if self.left.min_pair == self.min_pair:
            self.left = self.left.merge_min()
        elif self.left.right_most_value + self.right.left_most_value == self.min_pair:
            self.left.add_right(self.right.left_most_value)
            right = self.right.remove_left()
            if right is None:
                return self.left
            else:
                self.right = right
        else:
            self.right = self.right.merge_min()
        self._update_info()
        return self

    @classmethod
    def build(cls, nums, start, end):
        if start + 1 == end:
            return cls(None, None, nums[start])
        else:
            mid = (start + end) // 2
            return cls(cls.build(nums, start, mid), cls.build(nums, mid, end))

    def __repr__(self):
        if self.left is None:
            return f'[{self.left_most_value}]'
        else:
            return f'[{self.left} {self.right}]'


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ans = 0
        root = SegTree.build(nums, 0, len(nums))
        while not root.nondec:
            ans += 1
            root = root.merge_min()
        return ans

# 作者：灵剑2012
# 链接：https://leetcode.cn/problems/minimum-pair-removal-to-sort-array-ii/solutions/3643034/chun-xian-duan-shu-by-ling-jian-2012-bu47/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

re= Solution().minimumPairRemoval([5,2,3,1])
print(re)