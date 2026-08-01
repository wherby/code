# https://codeforces.com/gym/103643/problem/M
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0724/solution/cf103643m.md
# 因为 O(m) == O(n) 所以最后的candidate数量是很少的 O(sqrt(m))
# 对vis 进行标记恢复的算法，可以降低每次分配的开销
# 对出度为2，和3 的两种情况，考虑移除点和点对的贡献，记录对应的差分贡献值



import init_setting
from cflibs import *
def main():
    n, m, q = MII()
    
    degs = [n - 1] * n
    path = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v = GMI()
        
        degs[u] -= 1
        degs[v] -= 1
        
        path[u].append(v)
        path[v].append(u)
    
    vis = [0] * n
    
    base = 0
    diff = [0] * n
    
    for i in range(n):
        if degs[i] <= 1:
            base += 1
            diff[i] -= 1
    
    pairs = Counter()
    
    for i in range(n):
        if 2 <= degs[i] <= 3:
            vis[i] = 1
            for j in path[i]:
                vis[j] = 1
            
            tmp = []
            for j in range(n):
                if not vis[j]:
                    tmp.append(j)
            
            if degs[i] == 2:
                u, v = tmp
                diff[u] += 1
                diff[v] += 1
                pairs[(u, v)] -= 1
                
                if i < u: pairs[(i, u)] -= 1
                else: pairs[(u, i)] -= 1
                
                if i < v: pairs[(i, v)] -= 1
                else: pairs[(v, i)] -= 1
            else:
                u, v, w = tmp
                pairs[(u, v)] += 1
                pairs[(v, w)] += 1
                pairs[(u, w)] += 1
            
            vis[i] = 0
            for j in path[i]:
                vis[j] = 0
    
    outs = []
    
    for _ in range(q):
        u, v = GMI()
        if u > v: u, v = v, u
        
        ans = base + diff[u] + diff[v]
        if (u, v) in pairs: ans += pairs[(u, v)]
        
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))