from typing import List, Tuple, Optional

class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        size = int(n ** 0.5)
        sums = [0] * ((n + size - 1) // size)  # n/size 向上取整
        for i, num in enumerate(nums):
            sums[i // size] += num
        self.nums = nums
        self.sums = sums
        self.size = size

    def update(self, index: int, val: int) -> None:
        self.sums[index // self.size] += val - self.nums[index]
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        m = self.size
        b1, b2 = left // m, right // m
        if b1 == b2:  # 区间 [left, right] 在同一块中
            return sum(self.nums[left:right + 1])
        return sum(self.nums[left:(b1 + 1) * m]) + sum(self.sums[b1 + 1:b2]) + sum(self.nums[b2 * m:right + 1])

#作者：力扣官方题解
#链接：https://leetcode.cn/problems/range-sum-query-mutable/solutions/1389182/qu-yu-he-jian-suo-shu-zu-ke-xiu-gai-by-l-76xj/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。