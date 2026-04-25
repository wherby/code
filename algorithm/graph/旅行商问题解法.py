# https://codeforces.com/gym/105791/problem/M
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0416/solution/cf105791m.md
# 标准旅行商问题，在N <20的有向图上，求一个环形路径经过所有点的路径和最小
# 选择任意点 0 点开始，使用bitmask记录已经到的点 dp[j][i] 表示有向路径的终点 和访问过的点
# 然后再用 min(dp[i][(1 << n) - 1] + grid[i][0] for i in range(n))  遍历可能的终点和该点连回0起始点的路径和的最小值


import init_setting
from cflibs import *
def main():  
    n = II()
    grid = [LII() for _ in range(n)]
    
    if n == 1:
        print(0)
    else:
        inf = 10 ** 9
        dp = [[inf] * (1 << n) for _ in range(n)]
        dp[0][1] = 0
    
        for i in range(1 << n):
            for j in range(n):
                if dp[j][i] < inf:
                    for nj in range(n):
                        if i >> nj & 1: continue
                        ni = i | (1 << nj)
                        dp[nj][ni] = fmin(dp[nj][ni], dp[j][i] + grid[j][nj])
    
        print(min(dp[i][(1 << n) - 1] + grid[i][0] for i in range(n)))