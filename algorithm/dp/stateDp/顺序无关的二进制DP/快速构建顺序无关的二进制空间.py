# https://leetcode.cn/problems/partition-array-for-maximum-xor-and-and/solutions/3734850/shi-zi-bian-xing-xian-xing-ji-pythonjava-3e80/
# 这里DP值与元素的顺序无关， 所以可以用此方法快速构建dp空间
# 不用考虑  101111 -> 111111  因为元素顺序无关，所以 01111->11111 就包含了这个转移链是： 1111 -> 01111->101111 
# for i,a in enumerate(nums):
#     hibit = 1<<i
#     for mask in range(hibit):
#         sub_add[mask | hibit] = sub_add[mask] & a 
#         sub_xor[mask | hibit] = sub_xor[mask] ^a 
from typing import List, Tuple, Optional

class XorBasis:
    def __init__(self, n: int):
        self.b = [0] * n

    def insert(self, x: int) -> None:
        b = self.b
        for i in range(len(b) - 1, -1, -1):
            if x >> i & 1:
                if b[i] == 0:
                    b[i] = x
                    return
                x ^= b[i]

    def max_xor(self) -> int:
        b = self.b
        res = 0
        for i in range(len(b) - 1, -1, -1):
            if res ^ b[i] > res:
                res ^= b[i]
        return res


class Solution:
    def maximizeXorAndXor(self, nums: List[int]) -> int:
        n = len(nums)
        sz= max(nums).bit_length()

        u= 1<< n 
        sub_add =[0]*u 
        sub_xor = [0]*u 
        sub_add[0] = -1

        for i,a in enumerate(nums):
            hibit = 1<<i
            for mask in range(hibit):
                sub_add[mask | hibit] = sub_add[mask] & a 
                sub_xor[mask | hibit] = sub_xor[mask] ^a 
        sub_add[0] = 0 

        def max_xor2(sub):
            b = XorBasis(sz)
            xor = sub_xor[sub]
            for i,a in enumerate(nums):
                if sub>>i &1:
                    b.insert(a& ~xor)
            return b.max_xor() *2 +xor
        return max(sub_add[i] + max_xor2((u-1)^i) for i in range(u)) 





re =Solution().maximizeXorAndXor( [14,162,43])
print(re)