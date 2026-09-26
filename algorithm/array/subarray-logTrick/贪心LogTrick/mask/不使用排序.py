# https://leetcode.cn/contest/weekly-contest-520/problems/lexicographically-largest-power-array/description/
# 不使用排序，
# 按照mask 变化求取第2大的mask,得到贪心的下降路线
class Solution:
    def largestPower(self, nums: list[int]) -> list[int]:
        ans = [0] * 15
        mask = (1 << 15) - 1

        while mask:
            cnt = sum(x & mask == mask for x in nums)
            mx = 0
            for x in nums:
                res = x & mask
                if res != mask:
                    if res > mx:
                        mx = res

            for i in range(15):
                if (mask ^ mx) & (1 << i):
                    ans[14 - i] = cnt
            mask = mx
        return ans