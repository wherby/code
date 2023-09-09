# https://leetcode.cn/problems/minimum-time-to-repair-cars/solutions/2425409/xiu-che-de-zui-shao-shi-jian-by-leetcode-if20/?envType=daily-question&envId=2023-09-07
from typing import List, Tuple, Optional
from bisect import bisect_right,insort_left,bisect_left
import math
import bisect
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def f(t):
            return sum(math.floor(math.sqrt(t / r)) for r in ranks)
        return bisect.bisect_left(range(1_000_000_000_000_000), cars, key=f)


re = Solution().repairCars(ranks = [4,2,3,1], cars = 10)
print(re)