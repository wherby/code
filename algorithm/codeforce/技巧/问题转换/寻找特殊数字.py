# https://codeforces.com/gym/102319/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1008/solution/cf102319e.md
# 利用最小合数4，就能找到最少包含4个的边界，利用双指针方式就能找到边界

import init_setting
from cflibs import *
def main():
    def query(s):
        print('?', s, flush=True)
        return II()
    
    def answer(s):
        print('!', s)
    
    n, k = MII()
    
    ans = [0] * n
    bound = -1
    
    for i in range(4, n + 1):
        v = [0] * n
        for j in range(i):
            v[j] = 1
        
        if query(''.join(map(str, v))):
            bound = i
            ans = v
            break
    
    for j in range(bound):
        ans[j] = 0
        if not query(''.join(map(str, ans))):
            ans[j] = 1
    
    tmp = ans[:]
    tmp[bound - 1] = 0
    
    for j in range(bound, n):
        tmp[j] = 1
        if query(''.join(map(str, tmp))):
            ans[j] = 1
        tmp[j] = 0
    
    answer(''.join(map(str, ans)))