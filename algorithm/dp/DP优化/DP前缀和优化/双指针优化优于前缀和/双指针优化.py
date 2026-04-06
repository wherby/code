from typing import List, Tuple, Optional

MOD = 1_000_000_007
MX = 5001
MAX_DIGIT_SUM = 31  # 4999 的数位和最大
sum_to_nums = [[] for _ in range(MAX_DIGIT_SUM + 1)]
dig_sum = [0] * MX
for x in range(MX):
    # 去掉 x 的个位，问题变成 x // 10 的数位和，即 dig_sum[x // 10]
    dig_sum[x] = dig_sum[x // 10] + x % 10
    sum_to_nums[dig_sum[x]].append(x)

class Solution:
    def countArrays(self, digitSum: List[int]) -> int:
        f = [0] * MX  # f[x] 表示以 x 结尾的有效数组的个数
        f[0] = 1
        pre = 0

        for cur in digitSum:
            if cur > MAX_DIGIT_SUM:
                return 0
            a = sum_to_nums[pre]
            j, m = 0, len(a)
            s = 0
            for x in sum_to_nums[cur]:
                # 有效数组的前一个数只要 <= x 就行
                while j < m and a[j] <= x:
                    s += f[a[j]]
                    j += 1
                # s 现在就是以 x 结尾的有效数组的个数
                f[x] = s % MOD
            pre = cur  # 记录上一个数位和

        return sum(f[x] for x in sum_to_nums[pre]) % MOD

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/count-non-decreasing-arrays-with-given-digit-sums/solutions/3939449/liang-chong-fang-fa-qian-zhui-he-you-hua-dndq/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。