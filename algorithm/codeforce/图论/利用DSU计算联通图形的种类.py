# https://codeforces.com/gym/105971/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0403/solution/cf105971e.md
# 这里只有一类情况是会有两个可选点，如果其他点与其中一点连接起来，就可以用DSU把这些点记录为一个联通区域
# 如果只有一个点的选择，则认为是自联，这样也记录一条边数
# 在讨论的时候，如果边数大于点数，显然不满足，如果边数等于点数的时候，如果有自联的边，此时就完全固定了，如果没有自联的边，此时图只有两种分配方式
# 如果边数小于点数，而且又是联通图必然 边数+1 ==点数，此时只有一个可能就是当前图形是一颗树，此时树上任一点都可以是空着的，其他点的分配就固定了




import init_setting
from cflibs import *
from lib.UnionFind import * 
def main(): 
    t = II()
    outs = []
    
    mod = 10 ** 9 + 7
    
    for _ in range(t):
        n, m, k = MII()
        xs = []
        ys = []
        
        for _ in range(k + 1):
            x, y = GMI()
            xs.append(x)
            ys.append(y)
        
        flg = True
        for i in range(k):
            if abs(xs[i + 1] - xs[i]) + abs(ys[i + 1] - ys[i]) != 2:
                flg = False
        
        if not flg: outs.append(0)
        else:
            uf = UnionFind(n * m)
            edge_cnt = [0] * (n * m)
            self_cycle = [0] * (n * m)
            
            def f(x, y):
                return x * m + y
            
            for i in range(k):
                x1, y1 = xs[i], ys[i]
                x2, y2 = xs[i + 1], ys[i + 1]
    
                if x1 == x2 or y1 == y2:
                    msk = f((x1 + x2) // 2, (y1 + y2) // 2)
                    edge_cnt[msk] += 1
                    self_cycle[msk] = 1
                else:
                    msk1 = f(x1, y2)
                    msk2 = f(x2, y1)
                    uf.merge(msk1, msk2)
                    edge_cnt[msk1] += 1
            
            for i in range(n * m):
                if uf.find(i) != i:
                    edge_cnt[uf.find(i)] += edge_cnt[i]
                    self_cycle[uf.find(i)] |= self_cycle[i]
            
            ans = 1
            for i in range(n * m):
                if uf.find(i) == i:
                    if edge_cnt[i] > uf.getSize(i):
                        ans = 0
                    elif edge_cnt[i] == uf.getSize(i):
                        if not self_cycle[i]:
                            ans = ans * 2 % mod
                    else:
                        ans = ans * uf.getSize(i) % mod
            
            outs.append(ans)
    
    print('\n'.join(map(str, outs)))