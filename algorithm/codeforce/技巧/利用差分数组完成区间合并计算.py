# https://codeforces.com/problemset/problem/731/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0904/solution/cf731d.md
# 这里根据前后序列，每个前后序列都可能有一个连续区间或者两个在两边的区间，
# 问题是求最先满足所有区间的点，如果用区间合并的话，计算量会比较大？或者难写， 用差分数组计数则很容易解决

import init_setting
from cflibs import *
def main():
    n, c = MII()
    diff = [0] * (c + 1)
    
    k1 = 0
    v1 = []
    
    for _ in range(n):
        k2, *v2 = LII()
        
        for i in range(fmin(k1, k2)):
            if v1[i] != v2[i]:
                if v1[i] < v2[i]:
                    diff[0] += 1
                    diff[c - v2[i] + 1] -= 1
                    diff[c - v1[i] + 1] += 1
                    diff[c] -= 1
                else:
                    diff[c - v1[i] + 1] += 1
                    diff[c - v2[i] + 1] -= 1
                break
        else:
            if k1 > k2:
                exit(print(-1))
            else:
                diff[0] += 1
                diff[c] -= 1
        
        k1 = k2
        v1 = v2
    
    for i in range(c):
        diff[i + 1] += diff[i]
    
    for i in range(c + 1):
        if diff[i] == n:
            exit(print(i))
    
    print(-1)