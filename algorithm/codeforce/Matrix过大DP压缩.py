# https://codeforces.com/problemset/problem/1970/E3
#https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/05/0517/solution/cf1970e3.md
# 由于前一天的最后一段和后一天的第一段是关联的，所以 
#grid[A][B] :A 表示前一天是否限制为短路径，B表示后一天是否为短路径
#因为B中 0表示短路径，1表示长路径，所以按照矩阵乘法的特性，对于A,0则表示没有限制，1表示短路径

from cflibs import *
def main():
    n, k = MII()

    ss = LII()
    ls = LII()

    grid = [[0, 0], [0, 0]]

    for i in range(n):
        grid[0][0] = (grid[0][0] + (ls[i] + ss[i]) * ss[i]) % mod
        grid[0][1] = (grid[0][1] + (ls[i] + ss[i]) * ls[i]) % mod
        grid[1][0] = (grid[1][0] + ss[i] * ss[i]) % mod
        grid[1][1] = (grid[1][1] + ss[i] * ls[i]) % mod

    total_s = sum(ss) % mod
    total_l = sum(ls) % mod

    res = matrix_pow(grid, k - 1)

    ans = 0
    ans += (ss[0] * res[0][0] + ls[0] * res[1][0]) * (total_s + total_l)
    ans += (ss[0] * res[0][1] + ls[0] * res[1][1]) * total_s

    print(ans % mod)