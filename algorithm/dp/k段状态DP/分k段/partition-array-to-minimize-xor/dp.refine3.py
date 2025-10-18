# https://leetcode.cn/contest/weekly-contest-456/problems/partition-array-to-minimize-xor/description/
from typing import List, Tuple, Optional
from math import inf
# 手写 min max 更快
min = lambda a, b: b if b < a else a
max = lambda a, b: b if b > a else a

class Solution:
    def minXor(self, nums: List[int], k: int) -> int:
        n = len(nums)
        f = [[inf] * (n + 1) for _ in range(k + 1)]
        f[0][0] = 0
        for i in range(1, k + 1):
            # 前后每个子数组长度至少是 1，预留空间给这些子数组
            for j in range(i, n - (k - i) + 1):
                s = 0
                for l in range(j - 1, i - 2, -1):
                    s ^= nums[l]
                    f[i][j] = min(f[i][j], max(f[i - 1][l], s))
        return f[k][n]

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/partition-array-to-minimize-xor/solutions/3710966/hua-fen-xing-dp-de-tong-yong-tao-lu-pyth-lmcm/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


re =Solution().minXor( nums = [2,3,3,2,4]*50, k = 150)
print(re)