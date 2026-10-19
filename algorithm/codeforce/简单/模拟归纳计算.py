# https://codeforces.com/gym/101047/problem/M
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1005/solution/cf101047m.md


import init_setting
from lib.cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        s = [1 if c == 'D' else 0 for c in I()]
        
        if sum(s) % 2 == 0: outs.append('N')
        else:
            ans = []
            l = 0
            for i in range(n):
                if s[i]:
                    for j in range(i, l - 1, -1):
                        ans.append(j)
                    l = i + 1
                    if i + 1 < n:
                        s[i + 1] ^= 1
            
            outs.append('Y')
            outs.append(' '.join(str(x + 1) for x in ans))
    
    print('\n'.join(outs))