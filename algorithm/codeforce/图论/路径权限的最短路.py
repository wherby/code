#https://codeforces.com/gym/105811/problem/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0109/solution/cf105811j.md
# 到某点和某点返回的图就是原图和反图上求最短路，此时最短路的值是路径最大权限而已




import init_setting
from lib.cflibs import *
def main(): 
    inf = 2 * 10 ** 9
    
    def shortest_path(n, path):
        ans = [inf] * n
        ans[0] = 0
        
        pq = [0]
        while pq:
            d, u = divmod(heappop(pq), n)
            if ans[u] == d:
                for msk in path[u]:
                    nd, v = divmod(msk, n)
                    nd = fmax(d, nd)
                    if nd < ans[v]:
                        ans[v] = nd
                        heappush(pq, ans[v] * n + v)
        
        return ans
    
    n, m = MII()
    path = [[] for _ in range(n)]
    rev_path = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v, w = MII()
        u -= 1
        v -= 1
        path[u].append(w * n + v)
        rev_path[v].append(w * n + u)
    
    d1 = shortest_path(n, path)
    d2 = shortest_path(n, rev_path)
    
    for i in range(n):
        if d2[i] > d1[i]:
            exit(print('NO'))
    
    print('YES')