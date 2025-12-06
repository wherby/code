from typing import List, Tuple, Optional
from collections import defaultdict,deque

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 1_000_000_007
        n = len(nums)
        min_q = deque()
        max_q = deque()
        f = [0] * (n + 1)
        f[0] = 1
        sum_f = 0  # 窗口中的 f[i] 之和
        left = 0

        for i, x in enumerate(nums):
            # 1. 入
            sum_f += f[i]

            while min_q and x <= nums[min_q[-1]]:
                min_q.pop()
            min_q.append(i)

            while max_q and x >= nums[max_q[-1]]:
                max_q.pop()
            max_q.append(i)

            # 2. 出
            while nums[max_q[0]] - nums[min_q[0]] > k:
                sum_f -= f[left]
                left += 1
                if min_q[0] < left:
                    min_q.popleft()
                if max_q[0] < left:
                    max_q.popleft()

            # 3. 更新答案
            f[i + 1] = sum_f % MOD

        return f[n]

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/count-partitions-with-max-min-difference-at-most-k/solutions/3695716/hua-fen-xing-dp-dan-diao-dui-lie-you-hua-9rtj/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。