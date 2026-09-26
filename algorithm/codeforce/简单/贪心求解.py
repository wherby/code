# https://codeforces.com/gym/106677/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0901/solution/cf106677e.md


import init_setting
from lib.cflibs import *
def main():
    outs = []
    
    while True:
        n = II()
        if n == 0: break
        
        items = []
        
        for _ in range(n):
            w1, w2 = MII()
            items.append((w1, w2))
        
        must_buy = n - fmin(n - 1, sum(x[1] for x in items))
        
        items.sort()
        
        chosen = -1
        ans = 0
        
        for i in range(n):
            if items[i][1]:
                chosen = i
                must_buy -= 1
                ans += items[i][0]
                break
        
        for i in range(n):
            if must_buy and i != chosen:
                must_buy -= 1
                ans += items[i][0]
        
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))