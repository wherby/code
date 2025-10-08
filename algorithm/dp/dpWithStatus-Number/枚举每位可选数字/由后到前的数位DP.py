from functools import cache
# 返回两个 1~9 的整数和为 target 的方案数
def two_sum_ways(target: int) -> int:
    return max(min(target - 1, 19 - target), 0)  # 保证结果非负

class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        s = list(map(int, str(n)))
        m = len(s)

        # borrow = True 表示被低位（i+1）借位
        # is_num = True 表示之前填的数位，两个数都无前导零
        @cache
        def dfs(i: int, borrowed: bool, is_num: bool) -> int:
            if i < 0:
                # borrowed 必须为 False
                return 0 if borrowed else 1

            d = s[i] - borrowed

            # 其中一个数必须填前导零
            if not is_num:
                # 在 i > 0 的情况下，另一个数必须不为 0（否则可以为 0，即两个数的最高位都是 0）
                if i > 0 and d == 0:
                    return 0
                # 如果 d < 0，必须向高位借位
                return dfs(i - 1, d < 0, False)

            # 令其中一个数从当前位置开始往左都是 0（前导零）
            res = 0
            if i < m - 1:
                if d != 0:  # 另一个数不为 0
                    res = dfs(i - 1, d < 0, False) * 2  # 根据对称性乘以 2
                elif i == 0:  # 最高位被借走
                    res = 1  # 两个数都是 0
                # else res = 0

            # 两个数位都不为 0
            res += dfs(i - 1, False, True) * two_sum_ways(d)  # 不向 i-1 借位
            res += dfs(i - 1, True, True) * two_sum_ways(d + 10)  # 向 i-1 借位
            return res

        return dfs(m - 1, False, True)

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/count-no-zero-pairs-that-sum-to-n/solutions/3798539/cong-di-wang-gao-de-shu-wei-dppythonjava-r8dh/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。