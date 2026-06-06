# https://codeforces.com/gym/106523/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0604/solution/cf106523f.md
# 题目的意思是选择的 位置系数 * 参数系数 = 排列系数
# 由于 位置和 排列的个数一致， 则参数系数只有可能是单项式。
# 题目转换为列举参数的单项式值，查找满足当前系数差值的 位置 和排列的环有多少
# 题目中用最后一个dumb 数字连接不能构成环的所有链条



import init_setting
from cflibs import *
from lib.UnionFind import *
def main():
    n = II()
    nums = LGMI()
    
    mod = 998244353
    pw2 = [1] * (n + 1)
    
    for i in range(n):
        pw2[i + 1] = pw2[i] * 2 % mod
    
    ans = 0
    uf = UnionFind(n + 1)
    
    for i in range(n):
        uf.init()
    
        for j in range(n):
            uf.merge(j, fmin(nums[j] + i, n))
        
        cur = 0
        
        for j in range(n):
            if uf.find(j) == j and uf.find(j) != uf.find(n):
                cur += 1
        
        ans += pw2[cur] - 1
        ans %= mod
    
    print(ans)