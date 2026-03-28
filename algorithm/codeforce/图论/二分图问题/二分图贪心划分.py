# https://codeforces.com/gym/104009/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0321/solution/cf104009d.md
# UnionFind 恢复的时候，需要把所有路径一起恢复


import init_setting
from cflibs import *
from lib.UnionFindWithReset import UnionFind
def main(): 
    n, m = MII()
    dsu = UnionFind(n * 2)
    
    ans = 1
    cur = []
    
    for _ in range(m):
        u, v = GMI()
    
        if dsu.find(u) == dsu.find(v):
            for x in cur:
                dsu.back(x)
                dsu.back(x + n)
    
            ans += 1
            cur.clear()
    
        dsu.merge(u, v + n)
        dsu.merge(v, u + n)
    
        cur.append(u)
        cur.append(v)
    
    print(ans)

if __name__ == '__main__':
    main()
