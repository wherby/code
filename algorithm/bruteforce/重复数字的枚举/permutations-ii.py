
from typing import List, Tuple, Optional
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        path = [0] * n  # 所有排列的长度都是 n
        on_path = [False] * n  # on_path[j] 表示 nums[j] 是否已经填入排列

        # i 表示当前要填排列的第几个数
        def dfs(i: int) -> None:
            if i == n:  # 填完了
                ans.append(path.copy())  # 也可以写 path[:]
                return
            # 枚举 nums[j] 填入 path[i]
            for j, on in enumerate(on_path):
                # 如果 nums[j] 已填入排列，continue
                # 如果 nums[j] 和前一个数 nums[j-1] 相等，且 nums[j-1] 没填入排列，continue
                if on or j > 0 and nums[j] == nums[j - 1] and not on_path[j - 1]:
                    continue
                path[i] = nums[j]  # 填入排列
                on_path[j] = True  # nums[j] 已填入排列（注意标记的是下标，不是值）
                dfs(i + 1)  # 填排列的下一个数
                on_path[j] = False  # 恢复现场
                # 注意 path 无需恢复现场，因为排列长度固定，直接覆盖就行

        dfs(0)
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/permutations-ii/solutions/3059690/ru-he-qu-zhong-pythonjavacgojsrust-by-en-zlwl/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。