from functools import cache
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        high = list(map(int, str(high)))  # 避免在 dfs 中频繁调用 int()
        n = len(high)
        low = list(map(int, str(low).zfill(n)))  # 补前导零，和 high 对齐

        @cache
        def dfs(i: int, start: int, diff: int, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return 1 if diff == 0 else 0

            lo = low[i] if limit_low else 0
            hi = high[i] if limit_high else 9

            # 如果前面没有填数字，且剩余数位个数是奇数，那么当前数位不能填数字
            if start < 0 and (n - i) % 2:
                # 如果必须填数字（lo > 0），不合法，返回 0
                return 0 if lo else dfs(i + 1, start, diff, True, False)

            res = 0
            is_left = start < 0 or i < (start + n) // 2
            for d in range(lo, hi + 1):
                res += dfs(i + 1,
                           i if start < 0 and d else start,  # 记录第一个填数字的位置
                           diff + (d if is_left else -d),  # 左半 + 右半 -
                           limit_low and d == lo,
                           limit_high and d == hi)
            return res

        return dfs(0, -1, 0, True, True)

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/count-symmetric-integers/solutions/2424088/mei-ju-by-endlesscheng-oo2d/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。