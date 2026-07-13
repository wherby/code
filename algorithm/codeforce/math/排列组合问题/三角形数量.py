# https://codeforces.com/gym/105164/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0704/solution/cf105164d.md
# 这里是如果用不超过n的火柴棍能构成多少个形状不一致的三角形
# 采用所有可能的构造，减去不合法的，和重复的三角形
# 先去除不能构造成三角形的构造，假设z是长边，则不能构成三角形的有 3 * (xy_bound - 1) * xy_bound //2 个
# 这里用了一个巧妙的计算，如果 xy_bound 是奇数，则会有2被的重复，如果是偶数，则相等的时候只有1个，正好减去了两边相等的情况
# xy_bound = 2 时候， 2*1 //2 = 1 这时只有3种分布，长边z在三个可能点
# xy_bound =3 时, 3*2//2 =2 ,  这时只能分成(1,2),(2,1)两种，z 可以由三个插入点
# c2 计算的时候，去除了等边情况，如果等腰的时候，另一边有3个插入点，等边的时候，就只有一种选取点的可能性



import init_setting
from cflibs import *

def main():
    n = II()
    mod = 10 ** 9 + 7
    
    total = n * (n - 1) * (n - 2) // 6
    
    for z in range(1, n - 1):
        xy_bound = fmin(z, n - z)
        total -= 3 * (xy_bound - 1) * xy_bound // 2
    
    c1 = n // 3
    c2 = 0
    
    for z in range(1, n - 1):
        l = z // 2 + 1
        r = (n - z) // 2
        c2 += fmax(r - l + 1, 0) - (l <= z <= r)
    
    total -= c1 + 3 * c2
    print((total // 6 + c1 + c2) % mod)