# https://codeforces.com/problemset/problem/1255/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/06/0627/solution/cf1255c.md
# 从链条里取得初始状态，需要先获取两个链接点，第二个点通过遍历所有的key值找到

import sys
sys.path.append("..")
from cflibs.cflibs import *
def main():
    n = II()

    cnt = [0] * (n + 1)
    path = defaultdict(list)

    for i in range(n - 2):
        tmp = LII()
        tmp.sort()
        
        u, v, w = tmp
        cnt[u] += 1
        cnt[v] += 1
        cnt[w] += 1
        
        path[(u, v)].append(w)
        path[(u, w)].append(v)
        path[(v, w)].append(u)

    for i in range(n + 1):
        if cnt[i] == 1:
            ans = [i]
            
            for u, v in path:
                if u == i and cnt[v] == 2:
                    ans.append(v)
                    break
                if v == i and cnt[u] == 2:
                    ans.append(u)
                    break
            
            for i in range(n - 2):
                u, v = ans[-2], ans[-1]
                if u > v: u, v = v, u
                
                for w in path[(u, v)]:
                    if len(ans) == 2 or ans[-3] != w:
                        ans.append(w)
                        break
            
            print(' '.join(map(str, ans)))
            
            break