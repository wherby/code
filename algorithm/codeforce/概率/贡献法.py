# https://codeforces.com/gym/102964/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0822/solution/cf102964e.md
# 计算经过K步之后的所有间隔数目，最后数字的数目是间隔数目+1， 由于k>1所以每个间隔的贡献是符合概率分布 (x-1)/x
# 如果k=0,直接计算


import init_setting
from cflibs import *
def main():
    n, x, k = MII()
    nums = LII()
    
    mod = 10 ** 9 + 7
    
    if k:
        total = (n - 1) * pow(2, k, mod) % mod
        print((total + 1 - total * pow(x, -1, mod)) % mod)
    
    else:
        print(sum(nums[i] != nums[i - 1] for i in range(1, n)) + 1)