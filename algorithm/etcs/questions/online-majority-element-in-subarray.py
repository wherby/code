#https://leetcode.cn/problems/online-majority-element-in-subarray/
# https://leetcode.cn/problems/online-majority-element-in-subarray/solution/suiji-by-981377660lmt-fw82/
from typing import List, Tuple, Optional
from collections import defaultdict,deque
from bisect import bisect_right,insort_left,bisect_left
from random import randint
class MajorityChecker:
    def __init__(self, arr: List[int]):
        self.arr = arr
        self.indexes = defaultdict(list)  
        for i, num in enumerate(arr):
            self.indexes[num].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        """寻找闭区区间[left,right]中的绝对众数,调用 query 的次数最多为 1e4
        """
        ROUND = 20
        for _ in range(ROUND):
            index = randint(left, right)
            num = self.arr[index]
            count = bisect_right(self.indexes[num], right) - bisect_left(self.indexes[num], left)
            if count >= threshold:
                return num
        return -1