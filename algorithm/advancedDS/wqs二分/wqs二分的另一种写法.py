

from collections import deque
from math import inf
from itertools import accumulate

max = lambda a, b: b if b > a else a  # 手写 max 更快

class Solution:
    def maximumSum(self, nums: list[int], m: int, l: int, r: int) -> int:
        n = len(nums)
        s = list(accumulate(nums, initial=0))  # nums 的前缀和

        # 没有 m 约束，但每选一个子数组就要把元素和减少 k
        def dp_without_limit(k: int) -> tuple[int, int]:
            f = [(0, 0)] * (n + 1)  # (DP 值, 子数组个数)，其中子数组个数取反，方便比大小
            q = deque()
            res = (-inf, 0)

            for i in range(l, n + 1):
                # 1. 入
                j = i - l
                v = (f[j][0] - s[j], f[j][1])
                while q and (f[q[-1]][0] - s[q[-1]], f[q[-1]][1]) <= v:
                    q.pop()
                q.append(j)

                # 2. 更新答案
                j = q[0]
                choose = (f[j][0] - s[j] + s[i] - k, f[j][1] - 1)  # 注意子数组个数取反了，加一变成减一
                # choose 保证我们至少选了一个子数组
                res = max(res, choose)  # DP 值相等时，子数组个数小的更优

                # 更新 DP
                f[i] = max(f[i - 1], choose)

                # 3. 出，下一轮循环队首离开窗口
                if j <= i - r:
                    q.popleft()

            return res[0], -res[1]

        res, cnt = dp_without_limit(0)
        if cnt <= m:  # 直接满足题目要求
            return res

        # 现在专注于解决「选恰好 m 个子数组」的问题
        ans = 0
        pos_sum = sum(x for x in nums if x > 0)  # nums 中的正数之和
        left, right = 0, pos_sum + 1
        while left + 1 < right:
            k = (left + right) // 2
            res, cnt = dp_without_limit(k)
            if cnt <= m:
                ans = res + m * k  # 见题解【细节 1】
                right = k
            else:
                left = k
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximum-sum-of-m-non-overlapping-subarrays-ii/solutions/3980778/la-ge-lang-ri-song-chi-wqs-er-fen-python-m2iw/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。