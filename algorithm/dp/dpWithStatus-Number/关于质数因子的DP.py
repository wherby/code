# https://codeforces.com/gym/105666/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0414/solution/cf105666a.md
# 这个问题有两个阶段，对于一个数字k， 它的某一位数位 d>1 且 d 整除 k,则可以把 k 转换为 k//d 然后继续循环操作，看是否能到1 
# 这里如果去枚举 d 从2，到9，则好像也可以？
# 这里把数字生成 和数字验证分为了两个阶段
# 数字生成的时候，只用了质数因子，2,3,5,7，因为其他数字都可以用质数因子表示，
# 且{2,3,5,7} 是互质的，在生成被验证的数字的时候，不用担心会生成重复数字的可能
# 生成数字之后，需要验证是否备选数字能按照规则到1，则用反向DP的方式，从1开始，用2到9去乘，然后看下一个数字有没有对应的d作为其中一个数字


import init_setting
from cflibs import *
def main(): 
    possible_vals = [1]
    bound = II()
    
    for x in [2, 3, 5, 7]:
        for i in range(len(possible_vals)):
            cur = possible_vals[i]
            while cur * x <= bound:
                cur *= x
                possible_vals.append(cur)
    
    k = len(possible_vals)
    d = {v: i for i, v in enumerate(possible_vals)}
    
    dp = [0] * k
    dp[0] = 1
    
    for i in range(k):
        if dp[i]:
            for x in range(2, 10):
                if possible_vals[i] * x <= bound and str(x) in str(possible_vals[i] * x):
                    dp[d[possible_vals[i] * x]] = 1
    
    print(sum(dp))