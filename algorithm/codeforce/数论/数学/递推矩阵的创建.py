# https://codeforces.com/gym/105109/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0921/solution/cf105109d.md
# algorithm/codeforce/docs/math/递推矩阵的创建.md
# 题目中是乘法关系，取log 变成递推加法关系，创建递推矩阵
# 利用费马小定理，在求指数的时候需要 (mod -1) ，乘积的时候是 mod



import init_setting
from cflibs import *
from lib.max_pow import matrix_pow
def main():
    n, k = MII()
    nums = LII()

    if k <= n:
        print(nums[k - 1])
    else:
        mod = 10 ** 9 + 6

        grid = [[0] * n for _ in range(n)]

        grid[0] = nums

        for i in range(1, n):
            grid[i][i - 1] = 1

        res = matrix_pow(grid, k - n,mod)[0]
        
        ans = 1
        mod += 1
        
        for i in range(n):
            ans = ans * pow(nums[i], res[n - 1 - i], mod) % mod
        
        print(ans)

main()