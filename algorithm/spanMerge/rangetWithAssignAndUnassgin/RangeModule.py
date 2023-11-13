# 715 https://leetcode.cn/problems/range-module/description/?envType=daily-question&envId=2023-11-12
import bisect
class RangeModule:

    def __init__(self):
        self.left = []
        self.right = []

    def addRange(self, left: int, right: int) -> None:
        idx1 = bisect.bisect_left(self.right, left)   #第一个右边大于等于左边
        idx2 = bisect.bisect_right(self.left, right)  #第一个左边大于右边
        if idx1 == idx2:
            self.left.insert(idx1, left)
            self.right.insert(idx2, right)
        else:
            left = min(left, self.left[idx1])
            right = max(right, self.right[idx2 - 1])
            self.left = self.left[:idx1] + [left] + self.left[idx2:]
            self.right = self.right[:idx1] + [right] + self.right[idx2:]

    def queryRange(self, left: int, right: int) -> bool:
        idx = bisect.bisect_left(self.right, right)
        return idx < len(self.right) and self.left[idx] <= left

    def removeRange(self, left: int, right: int) -> None:
        idx1 = bisect.bisect_right(self.right, left)
        idx2 = bisect.bisect_left(self.left, right)
        if idx1 != idx2:
            l = ([self.left[idx1]] if self.left[idx1] < left else []) + ([right] if self.right[idx2 - 1] > right else [])
            r = ([left] if self.left[idx1] < left else []) + ([self.right[idx2 - 1]] if self.right[idx2 - 1] > right else [])
            self.left = self.left[:idx1] + l + self.left[idx2:]
            self.right = self.right[:idx1] + r + self.right[idx2:]