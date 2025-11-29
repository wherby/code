from typing import List, Tuple, Optional

from functools import cache


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        low_s = list(map(int, str(num1)))  # 避免在 dfs 中频繁调用 int()
        high_s = list(map(int, str(num2)))
        n = len(high_s)
        diff_lh = n - len(low_s)

        @cache
        def dfs(i: int, waviness: int, last_cmp: int, last_digit: int, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return waviness

            lo = low_s[i - diff_lh] if limit_low and i >= diff_lh else 0
            hi = high_s[i] if limit_high else 9

            res = 0
            is_num = not limit_low or i > diff_lh  # 前面是否填过数字
            for d in range(lo, hi + 1):
                # 当前填的数不是最高位，c 才有意义
                c = (d > last_digit) - (d < last_digit) if is_num else 0
                w = waviness
                if c * last_cmp < 0:  # 形成了一个峰或谷
                    w += 1
                res += dfs(i + 1, w, c, d, limit_low and d == lo, limit_high and d == hi)
            return res

        return dfs(0, 0, 0, 0, True, True)

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/total-waviness-of-numbers-in-range-ii/solutions/3839571/shang-xia-jie-shu-wei-dppythonjavacgo-by-74vp/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。