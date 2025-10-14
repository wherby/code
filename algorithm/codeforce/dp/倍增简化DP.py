# https://codeforces.com/gym/103855/problem/H
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/10/1013/solution/cf103855h.md
# 问题？为什么划分点到上一个可以被作为“峰”的点就够了。
#      这里我们需要理解 ans = ans * (i - pos + 1) % mod 倍增的含义
#      如果越过上一“峰”的划分点，这个划分属于ans 里包含的基础划分(上一个状态的划分)，在“峰” 点后的任意点划分都是基础划分的倍数


import init_setting
from lib.cflibs import *
def main():
    n = II()
    nums = LII()
    
    mod = 10 ** 9 + 7
    
    cur = 0
    pos = 0
    
    ans = 1
    
    for i in range(n):
        if nums[i] > cur:
            ans = ans * (i - pos + 1) % mod
            cur = nums[i]
            pos = i
    
    print(ans)