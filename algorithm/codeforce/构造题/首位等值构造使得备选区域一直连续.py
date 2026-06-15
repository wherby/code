# https://codeforces.com/gym/105757/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0611/solution/cf105757b.md
# 需要用 1到N的数字填，所以在计算到质数的时候，每次消耗[x,N]的数字就能保证消耗的数字是连续的，然后再设置上限N为x-1
# 把范围缩小为 1-X 的填字游戏，这样每次循环都是在一个完整的区域内进行一个更小规模的题目
# 技巧： 保证数据范围变成更小的递归条件


import init_setting
from lib.cflibs import *
def main():
    M = 10 ** 6 + 10
    isPrime = [1] * M
    isPrime[0] = 0
    isPrime[1] = 0
    
    for i in range(2, M):
        if isPrime[i]:
            for j in range(2 * i, M, i):
                isPrime[j] = 0
    
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
    
        ans = [0] * n
        l, r = 0, n - 1
        
        while n:
            for x in range(1, n + 1):
                if isPrime[n + x]:
                    
                    for i in range(x, n + 1):
                        if i > n + x - i: break
                        ans[l] = i
                        ans[r] = n + x - i
                        l += 1
                        r -= 1
                    
                    n = x - 1
                    break
        
        outs.append(' '.join(map(str, ans)))
    
    print('\n'.join(outs))