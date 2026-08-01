# https://leetcode.cn/problems/number-of-unique-xor-triplets-ii/description/?envType=daily-question&envId=2026-07-24
# 给你一个整数数组 nums 。
# XOR 三元组 定义为三个元素的异或值 nums[i] XOR nums[j] XOR nums[k]，其中 i <= j <= k。
# 返回所有可能三元组 (i, j, k) 中 不同 的 XOR 值的数量。

from typing import List
import math

def fwt_xor(a: List[int], rsh: int) -> None:
    """
    快速沃尔什变换（异或卷积）
    rsh: 右移位数，0 表示正向变换，1 表示反向变换（除以2）
    """
    n = len(a)
    length = 2
    half = 1
    while length <= n:
        for i in range(0, n, length):
            for j in range(half):
                u = a[i + j]
                v = a[i + j + half]
                a[i + j] = (u + v) >> rsh
                a[i + j + half] = (u - v) >> rsh
        length <<= 1
        half <<= 1


def fwt_xor3(a: List[int]) -> List[int]:
    """
    计算频率数组的三次异或卷积
    相当于统计所有三元组的异或值分布
    """
    # 正向变换
    fwt_xor(a, 0)
    
    # 在变换域中立方
    for i in range(len(a)):
        a[i] = a[i] * a[i] * a[i]
    
    # 反向变换（带缩放）
    fwt_xor(a, 1)
    
    return a

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        """
        返回所有可能三元组 (i, j, k) 中不同的 XOR 值的数量
        """
        if not nums:
            return 0

        # 找到数组中的最大值，确定需要的位数
        max_val = max(nums)
        # 计算需要的大小（2 的幂次）
        size = 1 << (max_val.bit_length())
        
        # 创建频率数组
        cnt = [0] * size
        for x in nums:
            cnt[x] += 1
        
        # 计算所有三元组的异或值分布
        result = fwt_xor3(cnt)
        
        # 统计不同的异或值数量
        ans = 0
        for c in result:
            if c > 0:
                ans += 1
        
        return ans