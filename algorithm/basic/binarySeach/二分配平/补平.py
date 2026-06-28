# https://leetcode.cn/problems/maximum-total-value/solutions/3986161/er-fen-di-m-da-jie-zhi-pythonjavacgo-by-genr5/
# (v - low - 1) 为了使得选择的数量少于m，所以把low+1作为下限，这样就一定能有剩余

class Solution:
    def maxTotalValue(self, value: list[int], decay: list[int], m: int) -> int:
        def check(low: int) -> bool:
            left_m = m
            for v, d in zip(value, decay):
                if v >= low:
                    left_m -= (v - low) // d + 1
                    if left_m < 0:  # 提前跳出循环
                        return True
            return False

        left, right = 0, max(value) + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid
            else:
                right = mid
        low = left

        ans = 0
        # 计算价值严格大于 low 的价值和，以及这些价值的个数
        for v, d in zip(value, decay):
            if v > low:
                k = (v - low - 1) // d + 1
                m -= k
                ans += (v * 2 - d * (k - 1)) * k
        ans //= 2  # 把除以 2 提到循环外面
        ans += m * low  # 剩余 m 次选的价值都是 low
        return ans % 1_000_000_007

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximum-total-value/solutions/3986161/er-fen-di-m-da-jie-zhi-pythonjavacgo-by-genr5/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。