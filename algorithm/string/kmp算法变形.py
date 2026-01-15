# https://codeforces.com/gym/105018/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0114/solution/cf105018a.md
# 题目中需要寻求一个最长前缀每位都不一样，就是目标值是反转当前前缀，使用KMP得到最大前缀匹配即可


import init_setting
from cflibs import *
def main(): 
    def prep(p):
        pi = [0] * len(p)
        j = 0
        for i in range(1, len(p)):
            while j != 0 and p[j] != p[i]:
                j = pi[j - 1]
            if p[j] == p[i]:
                j += 1
            pi[i] = j
        return pi
    
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        s = [int(c) for c in I()]
        
        s.append(-1)
        for i in range(n):
            s.append(s[i] ^ 1)
        
        outs.append(' '.join(map(str, prep(s)[n + 1:])))
    
    print('\n'.join(map(str, outs)))