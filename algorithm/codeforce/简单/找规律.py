# https://codeforces.com/gym/106631/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0731/solution/cf106631d.md
# Bob 只有一种情况能赢，就是在完成Alice前N-1的前缀的时候，BOB已经完成了N步


import init_setting
from lib.cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        s = I()
        
        flg = True
        for i in range(n - 1):
            if s[i] != s[0]:
                flg = False
        
        outs.append('Bob' if flg else 'Alice')
    
    print('\n'.join(outs))