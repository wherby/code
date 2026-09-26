# https://codeforces.com/gym/106197/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0914/solution/cf106197d.md
# 因为要匹配，所以需要从低到高贪心匹配每一位

import init_setting
from lib.cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n, k = MII()
        nums = [1 if c == '+' else -1 for c in I()]
        
        ans = []
        
        for i in range(n):
            if k % 2: k -= nums[i]; ans.append('#')
            else: ans.append('.')
            k //= 2
        
        outs.append(''.join(ans) if k == 0 else '-1')
    
    print('\n'.join(outs))