# https://leetcode.cn/contest/weekly-contest-526/problems/minimize-the-maximum-value-of-gcd-connected-array/description/
# 最小质因子
class Solution:
    # 返回 value 的最小质因子
    def min_prime_divisor(self, value: int) -> int:
        for p in range(2, isqrt(value) + 1):
            if value % p == 0:
                return p
        return value  # value 是质数或者 1

    def minimumMaxValue(self, n: int, index: int, value: int) -> int:
        min_p = self.min_prime_divisor(value)
        if value == 1 or value - min_p - (index - 1) * 2 <= 0:  # nums[0] <= 0
            return -1
        if index == n - 1:
            return value
        return value + min_p + (n - 2 - index) * 2


# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimize-the-maximum-value-of-gcd-connected-array/solutions/4051701/tan-xin-gou-zao-pythonjavacgo-by-endless-pk9j/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
