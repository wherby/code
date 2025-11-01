# https://codeforces.com/gym/106073/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1101/solution/cf106073f.md
# 因为对于所有概率，都可以分解为概率链，链的起点就是停在table处，后面都是订单，可以把所有动作都看作一个二叉树
# 对于订单序列的长链，用从后到前计算
# 概率的mod表示，用 inv

import init_setting
from cflibs import *
def main(): 
    n, q = MII()
    nums = LII()
    mod = 10 ** 9 + 7
    rev2 = (mod + 1) // 2
    
    ans = [0] * (n + 1)
    
    cur = 0
    for v in reversed(nums):
        ans[v] = (ans[v] + cur * rev2) % mod
        cur = (cur + v) * rev2 % mod
    
    ans[1] = (ans[1] + cur) % mod
    
    print(*ans[1:], sep='\n')


# testing 
mod = 10 ** 9 + 7
rev2 = (mod + 1) // 2
print(rev2,pow(2,-1,mod))
