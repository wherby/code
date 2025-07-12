# https://leetcode.cn/problems/the-earliest-and-latest-rounds-where-players-compete/solutions/825860/dpmei-ju-xia-yi-lun-liang-ming-xuan-shou-okfu/?envType=daily-question&envId=2025-07-12

from typing import List, Tuple, Optional
from functools import cache

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        @cache  # 缓存装饰器，避免重复计算 dfs（一行代码实现记忆化）
        def dfs(n: int, first: int, second: int) -> Tuple[int, int]:
            # AB 相遇
            if first + second == n + 1:
                return 1, 1

            # 保证 A 左边人数比 B 右边人数少
            # 注：题目已保证 first < second
            if first + second > n + 1:
                first, second = n + 1 - second, n + 1 - first

            m = (n + 1) // 2  # 下一回合人数
            # AB 之间保留 [min_mid, max_mid) 个人
            min_mid = 0 if second <= m else second - n // 2 - 1
            max_mid = second - first if second <= m else m - first
            earliest, latest = inf, 0

            for left in range(first):  # 枚举 A 左侧保留 left 个人
                for mid in range(min_mid, max_mid):  # 枚举 AB 之间保留 mid 个人
                    # 无需枚举 B 右侧保留多少个人，因为剩下的 m-2-left-mid 个人都在 B 右侧
                    e, l = dfs(m, left + 1, left + mid + 2)
                    earliest = min(earliest, e)
                    latest = max(latest, l)

            # 加上当前回合
            return earliest + 1, latest + 1

        return list(dfs(n, firstPlayer, secondPlayer))

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/the-earliest-and-latest-rounds-where-players-compete/solutions/825860/dpmei-ju-xia-yi-lun-liang-ming-xuan-shou-okfu/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。