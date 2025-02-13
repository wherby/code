from functools import cache

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        high_s = str(highLimit)
        n = len(high_s)
        low_s = str(lowLimit).zfill(n)  # 补前导零，和 high_s 对齐

        @cache
        def dfs(i: int, j: int, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return 0 if j else 1

            lo = int(low_s[i]) if limit_low else 0
            hi = int(high_s[i]) if limit_high else 9

            res = 0
            for d in range(lo, min(hi, j) + 1):  # 枚举当前数位填 d，但不能超过 j
                res += dfs(i + 1, j - d, limit_low and d == lo, limit_high and d == hi)
            return res

        return max(dfs(0, j, True, True) for j in range(1, 46))

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximum-number-of-balls-in-a-box/solutions/3073112/san-chong-fang-fa-bao-li-mei-ju-qian-zhu-kze9/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。