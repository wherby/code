# https://codeforces.com/problemset/problem/582/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/05/0524/solution/cf582c.md
# 这里求满足条件的子数组在循环数组的个数， 用满足调节的数字标记1， 然后用最大计数计算从循环节里能达到的长度，且max是n，最后计算对应长度为m时候，有多少个起点能满足
# #TAG#循环数组#
import sys
sys.path.append("..")
from cflibs.cflibs import *
def main():
    n = II()
    nums = LII()

    gcds = [math.gcd(i, n) for i in range(n)]

    ans = 0

    for i in range(1, n):
        if n % i == 0:
            ma = [0] * i
            for j in range(n):
                ma[j % i] = fmax(ma[j % i], nums[j])
            
            flg = [0] * (2 * n)
            calc = [0] * (n + 1)
            
            for j in range(n):
                if nums[j] == ma[j % i]:
                    flg[j] = 1
                    flg[j + n] = 1

            cur = 0
            for j in range(2 * n - 1, -1, -1):
                if flg[j]: cur += 1
                else: cur = 0
                if j < n:
                    calc[fmin(n, cur)] += 1
            
            for j in range(n - 1, -1, -1):
                calc[j] += calc[j + 1]
            
            for j in range(i, n, i):
                if gcds[j] == i:
                    ans += calc[j]

    print(ans)