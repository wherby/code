# https://github.com/Yawn-Sean/Daily_CF_Problems
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/05/0527/solution/cf105325b.md
# 代价函数与移动步数有关，所以把移动的步数变成层级DP，从高层到低层
# DP[i][x] 表示还有i步，当前在x这个点，这样设计就可以保证无论需要多少步，在dp[0][x]就能保证最后到x的时候的最小代价，使得各个源节点都收拢到同一层



import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    inf = 10 ** 9
    
    for _ in range(t):
        n, m = MII()
        path = [[] for _ in range(n)]
        
        for _ in range(m):
            u, v, w = MII()
            path[u].append(w * n + v)
        
        dp = [[inf] * n for _ in range(n)]
        
        for i in range(n): dp[i][0] = 0
        
        for i in range(n - 1, 0, -1):
            for j in range(n):
                for msk in path[j]:
                    w, nj = divmod(msk, n)
                    dp[i - 1][nj] = fmin(dp[i - 1][nj], dp[i][j] + i * w)
        
        outs.append(' '.join(map(str, (x if x < inf else -1 for x in dp[0][1:]))))
    
    print('\n'.join(outs))