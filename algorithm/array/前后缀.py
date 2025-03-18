from typing import List, Tuple, Optional
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        suf_min = [0] * n  # 后缀最小值
        suf_min[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suf_min[i] = min(suf_min[i + 1], nums[i])

        ans = 0
        pre_max = nums[0]  # 前缀最大值
        for i in range(1, n - 1):
            x = nums[i]
            # 此时 pre_max 表示 [0, i-1] 中的最大值
            if pre_max < x < suf_min[i + 1]:
                ans += 2
            elif nums[i - 1] < x < nums[i + 1]:
                ans += 1
            # 更新后 pre_max 表示 [0, i] 中的最大值
            pre_max = max(pre_max, x)
        return ans


# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/sum-of-beauty-in-the-array/solutions/1006001/qian-zhui-zui-da-zhi-hou-zhui-zui-xiao-z-h9qz/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。