# https://codeforces.com/gym/106511/problem/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/05/0502/solution/cf106511j.md
# 博弈先求出环的大小，再利用lcm 大小博弈，取对应的关系

import init_setting
from cflibs import *
def main():
    n = II()
    v1 = LGMI()
    v2 = LGMI()
    
    def find_cycles(x):
        vis = [0] * n
        possible = [0] * (n + 1)
        
        for i in range(n):
            if not vis[i]:
                cur = i
                cnt = 0
    
                while not vis[cur]:
                    vis[cur] = 1
                    cnt += 1
                    cur = x[cur]
                
                possible[cnt] = 1
        
        return [x for x in range(n + 1) if possible[x]]
    
    w1 = find_cycles(v1)
    w2 = find_cycles(v2)
    
    print(max(min(math.lcm(a, b) for b in w2) for a in w1))
