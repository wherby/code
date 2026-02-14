# https://codeforces.com/gym/104052/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0214/solution/cf104052b.md
# 霍尔定义的推广 ： 如果一个系统受到多种资源的限制，那么它能产出的总量，一定不会超过任何资源子集所能支持的最大上限。
# 所以解线性方程组不等式求最大解的问题，变成了遍历所有资源组合，然后让资源组合条件下，每个套餐最小值能得到的最大值，
# 最后取所以有资源组合的最大值的最小值。
# algorithm/mathA/霍尔婚配定理/资源分配.md



import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    tmp = [[2, 1, 1, 0], [2, 0, 2, 0], [1, 1, 2, 1]]
    inf = 10 ** 9
    
    for _ in range(t):
        nums = LII()
        
        ans = inf
        for i in range(16):
            cur = 0
            for j in range(4):
                if i >> j & 1:
                    cur += nums[j]
            
            to_check = inf
            
            for j in range(3):
                val = 0
                for k in range(4):
                    if i >> k & 1:
                        val += tmp[j][k]
                to_check = fmin(to_check, val)
            
            if to_check: ans = fmin(ans, cur // to_check)
    
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))