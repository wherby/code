# 104855D - State Compression https://codeforces.com/gym/104855/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0221/solution/cf104855d.md
# 如果记录到达边颜色和点的状态组合则是N**2 的状态，因为题目中需要的是不同颜色的边，则这个条件只要有两种不同颜色边到这个点就能满足，可以向下传递，所以状态压缩成2**N 就能满足题目要求了
# 然而在条件满足的时候，并不是做了特别标记，而是在原图上做了双层网络，这样在访问的时候，每个点的复杂度就是O(1)了，整体复杂度是O(N+M)，非常高效
# 对于任意一个点，必然是填入第一层，然后再填第2层，所以这个双层网络本身也是压缩的，不会有2倍系数在每个点产生



import init_setting
from cflibs import *

def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n, m = MII()
        path = lst_lst(n)
        
        def f(x, y): return x * n + y
        
        for _ in range(m):
            u, v, c = GMI()
            path.append(u, f(c, v))
        
        vis = [[-2] * n for _ in range(2)]
        vis[0][0] = -1
        vis[1][0] = -1
        
        que = [0]
        
        for msk in que:
            u, time = divmod(msk, 2)
            
            for edge in path.iterate(u):
                c, v = divmod(edge, n)
                
                if vis[time][u] != c:
                    if vis[0][v] == -2:
                        vis[0][v] = c
                        que.append(2 * v)
                    elif vis[0][v] == c:
                        continue
                    elif vis[1][v] == -2:
                        vis[1][v] = c
                        que.append(2 * v + 1)
        
        outs.append(' '.join(str(i + 1) for i in range(n) if vis[0][i] != -2))
    
    print('\n'.join(outs))