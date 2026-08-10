# https://codeforces.com/gym/106632/problem/H
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0804/solution/cf106632h.md
# 这里在贪心的时候，记录了可以在将来使用to_fill， 并且在 to_fill没有的时候使用反悔贪心
# 也可以用sortedList来贪心求解


import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        v1 = LII()
        v2 = LII()
        
        cnt = [0] * n
        
        for x in v1:
            if x <= n:
                cnt[x - 1] += 1
        
        to_fill = 0
        
        total = 0
        pq = []
        
        for i in range(n):
            if cnt[i]:
                to_fill += cnt[i] - 1
                total += v2[i]
                heappush(pq, v2[i])
    
            elif to_fill:
                to_fill -= 1
                total += v2[i]
                heappush(pq, v2[i])
            
            elif pq and pq[0] < v2[i]:
                total += v2[i] - pq[0]
                heapreplace(pq, v2[i])
        
        outs.append(total)
    
    print('\n'.join(map(str, outs)))