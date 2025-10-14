# https://leetcode.cn/problems/find-sum-of-array-product-of-magical-sequences/?envType=daily-question&envId=2025-10-12
# 在num中选m个数，并且选中数的序号对应的二进制之和有k个置位,并且所有选择中的选中数字的乘积和
# 要满足选择 m个数字，选择中的序号对应的二进制之和有k个置位，
# 则从0,到n-1 递归选择数字，选到n序列的时候，应该有m个数字被选中，并且有k个置位和，二进制递归的时候计算当前余数
# 因为计算乘积和的同时求了排列的数量，在多次选择数字的时候，用逆元的方式先去除重复影响
from typing import List, Tuple, Optional
from functools import cache

mod = 10**9+7
MX=31
fac = [1]*MX
for i in range(1,MX):
    fac[i] = fac[i-1]*i%mod
inv_f =[1]*MX
inv_f[MX-1] = pow(fac[MX-1],mod-2,mod)
for i in range(MX-2,-1,-1):
    inv_f[i] = inv_f[i+1]*(i+1)%mod

class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(idx,leftM,leftK,acc):
            if idx ==n:
                return 1 if leftM ==0 and acc.bit_count()==leftK else 0
            ret = 0
            for i in range(leftM+1):
                accN = acc + i
                bitSet = accN%2 
                ret += pow(nums[idx],i,mod)*dfs(idx+1,leftM - i, leftK-bitSet,accN>>1)* inv_f[i]
            return ret%mod 
        return dfs(0,m,k,0)*fac[m]%mod