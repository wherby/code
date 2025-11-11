# 如果DP的时候，改变了当前操作数，则状态会多N个状态。所以需要让当前操作数不变 contest/00000c443d154/d169/q3
# https://leetcode.com/contest/biweekly-contest-169/problems/longest-non-decreasing-subarray-after-replacing-at-most-one-element/submissions/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        f = [[0, 0] for _ in range(n)]
        f[0] = [1, 1]

        ans = 1  # 以 nums[0] 结尾的子数组长度
        for i in range(1, n):
            if nums[i - 1] <= nums[i]:
                f[i][0] = f[i - 1][0] + 1
                f[i][1] = f[i - 1][1] + 1
            else:
                f[i][0] = 1
                # 不需要写 f[i][1] = 1，因为下面算出来的值至少是 2

            if i >= 2 and nums[i - 2] <= nums[i]:
                f[i][1] = max(f[i][1], f[i - 2][0] + 2)
            else:
                f[i][1] = max(f[i][1], 2)

            ans = max(ans, f[i - 1][0] + 1, f[i][1])
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/longest-non-decreasing-subarray-after-replacing-at-most-one-element/solutions/3826957/liang-chong-fang-fa-qian-hou-zhui-fen-ji-on94/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。