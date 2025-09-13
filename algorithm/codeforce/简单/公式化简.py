# https://codeforces.com/gym/104805/problem/K
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0910/solution/cf104805k.md
# 选择每个元素，总和的影响是 fn+1 = (fn +1) *(1+a) -1  对于L 直接先加上1 
# algorithm/mathA/组合数学/结论/二项式定理/所有子序列乘积和.py

import init_setting
from lib.cflibs import *
def main():
    n, l = MII()
    l += 1
    
    nums = LII()
    nums = list(set(nums))
    
    vis = {1}
    que = [1]
    
    for x in que:
        for v in nums:
            nx = x * (v + 1)
            if nx <= l and nx not in vis:
                vis.add(nx)
                que.append(nx)
    
    print(len(vis) - 1)