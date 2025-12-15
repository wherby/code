# 
# 在退位的时候生成的值可能不是回文  #  0b11110 32 6 3
# 但是不影响最后结果

from typing import List, Tuple, Optional
from math import inf




class Solution:
    def minOperations(self, nums: List[int]) -> List[int]:
        for i, x in enumerate(nums):
            res = inf
            n = x.bit_length()
            m = n // 2
            left = x >> m
            for l in range(left - 1, left + 2):
                # 左半反转到右半
                right = self.reverseBits(l >> (n % 2)) >> (32 - m)
                pal = l << m | right
                res = min(res, abs(x - pal))
                print(bin(pal),x,right,l)
            nums[i] = res
        return nums

    # 190. 颠倒二进制位
    # https://leetcode.cn/problems/reverse-bits/
    def reverseBits(self, n: int) -> int:
        # 交换 16 位
        n = ((n >> 16) | (n << 16)) & 0xFFFFFFFF
        # 交换每个 8 位块
        n = (((n & 0xFF00FF00) >> 8) | ((n & 0x00FF00FF) << 8)) & 0xFFFFFFFF
        # 交换每个 4 位块
        n = (((n & 0xF0F0F0F0) >> 4) | ((n & 0x0F0F0F0F) << 4)) & 0xFFFFFFFF
        # 交换每个 2 位块
        n = (((n & 0xCCCCCCCC) >> 2) | ((n & 0x33333333) << 2)) & 0xFFFFFFFF
        # 交换相邻位
        n = (((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)) & 0xFFFFFFFF
        return n

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-operations-to-make-binary-palindrome/solutions/3850779/fei-bao-li-zuo-fa-pythonjavacgo-by-endle-3gi2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
re = Solution().minOperations(nums = [6,7,12,32])