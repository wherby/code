# https://codeforces.com/gym/106795/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1030/solution/cf106795d.md
# 有意思的题目
# 这里考虑合并的时候不能直接用堆栈来模拟，但是可以考虑，最终的状态一定是交叉排列的，但是在任何一个合并的左右端点，如果左右端点都有，则合并可以用左右端点和合并项先合并，所以如果有合并的项，则这个项不能同时有左右端点一起在最终状态
#

import init_setting
from lib.cflibs import *
def main(): 
    n = II()
    s = I()
    
    if all(s[i] != s[i - 1] for i in range(1, n)): print(n)
    else:
        cur = 0
        
        for x in s:
            if x == 'G': cur += 1
            else: cur += 2
            cur %= 3
        
        print(1 if cur else 2)