
from typing import List, Tuple, Optional

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        path = []

        def dfs(i: int) -> None:
            if i == n:
                ans.append(path.copy())  # 也可以写 path[:]
                return

            # 选 x
            x = nums[i]
            path.append(x)
            dfs(i + 1)
            path.pop()  # 恢复现场

            # 不选 x，那么后面所有等于 x 的数都不选
            # 如果不跳过这些数，会导致「选 x 不选 x'」和「不选 x 选 x'」这两种情况都会加到 ans 中，这就重复了
            i += 1
            while i < n and nums[i] == x:
                i += 1
            dfs(i)

        dfs(0)
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/subsets-ii/solutions/3036436/liang-chong-fang-fa-xuan-huo-bu-xuan-mei-v0js/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。