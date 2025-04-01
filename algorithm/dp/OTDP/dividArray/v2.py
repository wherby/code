from typing import List, Tuple, Optional
from functools import cache
from itertools import accumulate

class Solution:
    def minimumCost(self, nums: List[int], cost: List[int], k: int) -> int:
        n = len(nums)
        s = list(accumulate(cost, initial=0))  # cost 的前缀和
        f = [0] * (n + 1)
        for i, sum_num in enumerate(accumulate(nums), 1):  # 这里把 i 加一了，下面不用加一
            f[i] = min(f[j] + sum_num * (s[i] - s[j]) + k * (s[n] - s[j])
                       for j in range(i))
        return f[n]

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-cost-to-divide-array-into-subarrays/solutions/3633352/hua-fen-xing-dp-shi-zi-bian-xing-pythonj-cwi9/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


re =Solution().minimumCost(nums = [3,1,4], cost = [4,6,6], k = 1)
print(re)