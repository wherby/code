from functools import cache

class Solution:
    def countLargestGroup(self, n: int) -> int:
        s = list(map(int, str(n)))  # 避免在 dfs 中频繁调用 int()
        m = len(s)

        @cache
        def dfs(i: int, left: int, limit_high: bool) -> int:
            if i == m:
                return 1 if left == 0 else 0
            hi = s[i] if limit_high else 9  # 当前数位至多填 hi
            res = 0
            for d in range(min(hi, left) + 1):  # 枚举当前数位填 d
                res += dfs(i + 1, left - d, limit_high and d == hi)
            return res

        max_cnt = ans = 0
        for target in range(1, m * 9 + 1):  # 枚举目标数位和
            cnt = dfs(0, target, True)
            if cnt > max_cnt:
                max_cnt = cnt
                ans = 1
            elif cnt == max_cnt:
                ans += 1
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/count-largest-group/solutions/3648666/liang-chong-fang-fa-bao-li-mei-ju-shu-we-g00u/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。