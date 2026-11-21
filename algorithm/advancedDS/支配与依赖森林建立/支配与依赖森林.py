# https://leetcode.cn/problems/count-non-decreasing-subarrays-after-k-operations/description/?envType=daily-question&envId=2026-11-13

# 给你一个长度为 n 的数组 nums 和一个整数 k 。
# 对于 nums 中的每一个子数组，你可以对它进行 至多 k 次操作。每次操作中，你可以将子数组中的任意一个元素增加 1 。
# 注意 ，每个子数组都是独立的，也就是说你对一个子数组的修改不会保留到另一个子数组中。
# 请你返回最多 k 次操作以内，有多少个子数组可以变成 非递减 的。
# 如果一个数组中的每一个元素都大于等于前一个元素（如果前一个元素存在），那么我们称这个数组是 非递减 的。


# g 其实是一个支配森林， 表示每个节点能影响和支配节点的范围
# pos_r 则是支配节点的影响边界
# 双指针窗口计算

from typing import List, Tuple, Optional
from collections import defaultdict, deque


class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        g = [[] for _ in range(n)]
        pos_r = [n] * n
        st = []
        for i, x in enumerate(nums):
            while st and x >= nums[st[-1]]:
                pos_r[st[-1]] = i
                st.pop()
            # 左边大于x的最近元素，
            if st:
                g[st[-1]].append(i)
            st.append(i)
        ans = cnt = window_left = 0
        q = deque([])
        for window_r, x in enumerate(nums):
            while q and nums[q[-1]] <= x:
                q.pop()
            q.append(window_r)
            cnt += max(nums[q[0]] - x, 0)

            while cnt > k:
                out = nums[window_left]
                for i in g[window_left]:
                    if i > window_r:
                        break
                    cnt -= (out - nums[i]) * (min(pos_r[i], window_r + 1) - i)
                window_left += 1

                if q[0] < window_left:
                    q.popleft()
            ans += window_r - window_left + 1
        return ans
