
from typing import List, Tuple, Optional

MOD = 1_000_000_007
MX = 5001
MAX_DIGIT_SUM = 31  # 4999 的数位和最大
dig_sum = [0] * MX

# 预处理数位和
for x in range(MX):
    # 去掉 x 的个位，问题变成 x // 10 的数位和，即 dig_sum[x // 10]
    dig_sum[x] = dig_sum[x // 10] + x % 10

class Solution:
    def countArrays(self, digitSum: List[int]) -> int:
        s = [1] * MX  # f 的前缀和
        for ds in digitSum:
            if ds > MAX_DIGIT_SUM:
                return 0
            for x in range(MX):
                # 如果 dig_sum[x] != ds，那么 f[x] = 0，否则 f[x] = s[x]
                # 把 f[x] 的值填到 s[x] 中，那么只需要把 dig_sum[x] != ds 的 s[x] 置为 0
                if dig_sum[x] != ds:
                    s[x] = 0
                if x > 0:
                    s[x] = (s[x] + s[x - 1]) % MOD
        return s[-1]

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/count-non-decreasing-arrays-with-given-digit-sums/solutions/3939449/liang-chong-fang-fa-qian-zhui-he-you-hua-dndq/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。