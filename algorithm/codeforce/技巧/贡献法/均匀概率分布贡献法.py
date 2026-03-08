

class Solution:
    def sumOfNumbers(self, l: int, r: int, k: int) -> int:
        MOD = 1_000_000_007
        m = r - l + 1
        return (l + r) * m * (pow(10, k, MOD) - 1) * pow(18, -1, MOD) * pow(m, k - 1, MOD) % MOD

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/sum-of-k-digit-numbers-in-a-range/solutions/3910668/gong-xian-fa-shu-xue-gong-shi-pythonjava-qek9/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。