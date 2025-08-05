# https://codeforces.com/problemset/problem/33/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0804/solution/cf33c.md
# 无论怎么设置前后缀， 都会有 -+-三段状态， 也可能--状态也变成-状态，从结果来说都就变成三个状态转换
# 因为三个状态都是前向后转换，所以后面的状态要先计算，这样就可以跳过前面的状态选择

import init_setting
from lib.cflibs import *
def main():
    n = II()
    nums = LII()
    
    dp1, dp2, dp3 = 0, 0, 0
    for x in nums:
        dp3 = fmax(dp2, dp3) - x
        dp2 = fmax(dp1, dp2) + x
        dp1 -= x
    
    print(max(dp1, dp2, dp3))