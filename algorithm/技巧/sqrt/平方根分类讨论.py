# 利用平方根思想，把操作分为高频和低频操作，低频操作就直接模拟，高频操作用差分标记处理。
# 高频操作只占 isqrt(n) 种
from typing import List, Tuple, Optional
from math import isqrt
from functools import reduce,xor
from operator import ior, iand,ixor

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 1_000_000_007
        n = len(nums)
        B = 100
        diff = [None] * B

        for l, r, k, v in queries:
            if k < B:
                # 懒初始化
                if not diff[k]:
                    diff[k] = [1] * (n + k)
                diff[k][l] = diff[k][l] * v % MOD
                r = r - (r - l) % k + k
                diff[k][r] = diff[k][r] * pow(v, -1, MOD) % MOD
            else:
                for i in range(l, r + 1, k):
                    nums[i] = nums[i] * v % MOD

        for k, d in enumerate(diff):
            if not d:
                continue
            for start in range(k):
                mul_d = 1
                for i in range(start, n, k):
                    mul_d = mul_d * d[i] % MOD
                    nums[i] = nums[i] * mul_d % MOD

        return reduce(xor, nums)

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/xor-after-range-multiplication-queries-ii/solutions/3755296/gen-hao-suan-fa-pythonjavacgo-by-endless-moxx/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。