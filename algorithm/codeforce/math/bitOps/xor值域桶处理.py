# https://codeforces.com/gym/102331/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1008/solution/cf102331b.md
# xor 在值域桶里，取任意两个不同的桶的数字都大于 x，所以这里需要找到x 对应的桶大小bit
# 然而在同一个桶里的数字，最多能有2个的xor值会大于x, 因为x的最高位决定了bit桶的次高位，所以需要在同一个桶里计算可以被同时选中的组合数量


import init_setting
from cflibs import *
from lib.trie01 import Trie01
def main():
    n, x = MII()
    nums = LII()
    nums.sort()
    
    mod = 998244353
    
    if x == 0:
        print(pow(2, n, mod) - 1)
    else:
        k = x.bit_length()
        bit = 1 << k
    
        def solve(l, r):
            trie = Trie01(bit)
            res = r - l + 1
            cnt = 0
            
            for i in range(l, r):
                res += cnt - trie.count_lt_xor(nums[i],x)
                res %= mod
                
                cnt += 1
                trie.insert(nums[i])
            
            return res
    
        ans = 1
        l = 0
    
        for i in range(n):
            if nums[i] // bit != nums[l] // bit:
                ans = ans * solve(l, i) % mod
                l = i
    
        ans = ans * solve(l, n) % mod
        print((ans - 1) % mod)

main()