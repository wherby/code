# https://leetcode.cn/problems/pizza-with-3n-slices/
from typing import List, Tuple, Optional
from collections import defaultdict

class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        k = len(slices)//3
        def getMax(ls):
            n = len(ls)
            dp = defaultdict(int)
            for i in range(n):
                for j in range(k):
                    dp[(i,j)] = max(dp[(i-1,j)], dp[(i-2,j-1)] + ls[i]) # 根本问题是取得非连续的k个值的最大值
            return dp[(n-1,k-1)]
        return max(getMax(slices[:-1]),getMax(slices[1:])) # for 不能同时取最后一个和第一个，所以用两种方式


re = Solution().maxSizeSlices([9,5,1,7,8,4,4,5,5,8,7,7])
print(re)

