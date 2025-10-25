# https://codeforces.com/gym/105129/problem/L
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/10/1020/solution/cf105129l.md
# 找一个数与数组中数字的GCD>2
# 因为数组数字值域较小，就用所有质数，搜索集合作为备选项和数组的数字看是否集合能与所有数组的质因子都有交集


import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    prs = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    
    to_check = [1]
    for x in prs:
        for i in range(len(to_check)):
            to_check.append(to_check[i] * x)
    
    to_check.sort()
    
    for _ in range(t):
        n = II()
        nums = LII()
        
        vis = [0] * 51
        for x in nums:
            vis[x] = 1
        
        for v in to_check:
            for i in range(51):
                if vis[i] and math.gcd(i, v) == 1:
                    break
            else:
                outs.append(v)
                break
    
    print('\n'.join(map(str, outs)))