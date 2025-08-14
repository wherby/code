# https://codeforces.com/problemset/problem/1041/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0811/solution/cf1041e.md
# 其实构造的是一个链，简单树， 用max_flg 标记已经出现的节点，然后用cur把未出现的小节点加入到链表中。

import init_setting
from lib.cflibs import *
def main():
    n = II()
    cnt = [0] * (n + 1)
    max_flg = [0] * (n + 1)
    
    for _ in range(n - 1):
        u, v = MII()
        if v != n: exit(print('NO'))
        cnt[u] += 1
        max_flg[u] = 1
    
    chain = []
    cur = 1
    
    for i in range(1, n):
        if cnt[i]:
            cnt[i] -= 1
            
            chain.append(i)
            while cnt[i]:
                while max_flg[cur]:
                    cur += 1
                if cur > i:
                    exit(print('NO'))
                chain.append(cur)
                cur += 1
                cnt[i] -= 1
            
    chain.append(n)
    
    print('YES')
    print('\n'.join(f'{chain[i - 1]} {chain[i]}' for i in range(1, n)))