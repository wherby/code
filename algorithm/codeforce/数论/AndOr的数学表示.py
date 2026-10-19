# https://codeforces.com/gym/103627/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1006/solution/cf103627c.md
# 把 and 和Or 的 关系变成正交分量的表示法，原题变成了一个求凸曲线的一个点，由于如果图形有任意一点是凸的，则一定有一个正交分量是凸的
# algorithm/codeforce/docs/basic/AndOr的可枚举性.md

import init_setting
from cflibs import *
def main():
    n = II()
    nums = LII()
    
    for i in range(1 << n):
        bit1 = [1 << j for j in range(n) if i >> j & 1]
        bit2 = [1 << j for j in range(n) if not i >> j & 1]
        
        for b1 in bit1:
            for b2 in bit2:
                if nums[i - b1] + nums[i + b2] > nums[i] + nums[i - b1 + b2]:
                    print(i, i - b1 + b2)
                    exit()
    
    print(-1)