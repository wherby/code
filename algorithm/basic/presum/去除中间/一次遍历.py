from typing import List, Tuple, Optional

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        x = sum(nums) % p
        if x == 0:
            return 0  # 移除空子数组（这行可以不要）

        ans = n = len(nums)
        s = 0
        last = {s: -1}  # 由于下面 i 是从 0 开始的，前缀和下标就要从 -1 开始了
        for i, v in enumerate(nums):
            s += v
            last[s % p] = i
            j = last.get((s - x) % p, -n)  # 如果不存在，-n 可以保证 i-j >= n
            ans = min(ans, i - j)  # 改成手写 min 会再快一些
        return ans if ans < n else -1

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/make-sum-divisible-by-p/solutions/2158435/tao-lu-qian-zhui-he-ha-xi-biao-pythonjav-rzl0/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。