# https://codeforces.com/gym/105746/problem/C
# https://codeforces.com/gym/105746/attachments/download/30198/statements.pdf
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0413/solution/cf105746c.md
# 因为有向图图遍历的时候，两点之间有多条路径，这样得到的路径数量是指数倍数增加的，但是由于每个路径的斜率为{-1,0,1} 
# 而且图没有环，所以每条路径的总斜率在(-n,n)之间，所以可以用DP来记录斜率固定时候的最小截距
# 然而为了查询X点路径的在[L,R]上的最小值，因为代价函数是直线，所以可以用下凸包来记录candidate ： algorithm/mathA/凸包问题/docs/使用凸包维护线段在区间的最小值.md
# 而有了下凸包维护的 备选线段， 在[l,r]之间的最小值，就可以使用二分查找在端点 l,r 上的最小备选值线段
# **图论**（DAG）到**代数**（线性函数）再到**几何**（凸包优化）

# 你的理解完全正确！这个逻辑链条非常严密，已经把这道题从**图论**（DAG）到**代数**（线性函数）再到**几何**（凸包优化）的转化过程全部打通了。

# 我们可以把你的理解提炼为三个核心“降维”步骤：

# ### 1. 状态降维：利用斜率范围限制
# * **痛点**：两点间路径成千上万，甚至呈指数级增长。
# * **突破口**：因为是 **DAG**，路径长度受限于 $n-1$。如果边的斜率是小常数，总斜率 $k$ 的范围就是有限的（$|k| < n$）。
# * **操作**：用 `dp[city][slope]` 记录。这本质上是把“路径”降维成了“状态”，在每个节点对相同斜率的路径进行了**贪心去重**。

# ### 2. 几何降维：利用下凸包筛选备选线（Candidate Lines）
# * **痛点**：即使每个斜率只留一条线，每个城市依然有 $O(n)$ 条直线。对于每一个查询，遍历所有直线太慢。
# * **突破口**：我们只关心在某个时间点 $t$ 能取得**最小值**的直线。
# * **操作**：构建**下凸包**。这实际上是把 $O(n)$ 条直线进一步压缩成了只有“露脸机会”的少数几条备选线。


# ### 3. 查询降维：利用凹函数端点最值性
# * **痛点**：客户给的是一个时间区间 $[L, R]$，理论上需要检查区间内每一个时刻的最小值。
# * **突破口**：下凸包（多个线性函数取 $\min$）构成的函数是**凹函数**。
# * **操作**：因为凹函数的极小值必在端点取得，所以只需要在 $t=L$ 和 $t=R$ 处各做一次**二分查找**，取较小值即可。


# ---

# ### 总结
# 你现在的理解已经能够完美复现这套解法了：
# 1.  **拓扑 DP**：解决路径爆炸问题（$O(M \cdot N)$）。
# 2.  **凸包构建**：解决线段冗余问题（$O(N^2)$）。
# 3.  **端点二分**：解决区间查询效率问题（$O(Q \log N)$）。

# 这种把“最短路”和“计算几何”结合的思路，是处理**参数化边权**（Edge weights as functions）问题的经典套路。即便以后斜率不是小的常数，你也可以用“李超线段树”来替换第一步的 DP，核心逻辑依然是一致的。




import init_setting
from cflibs import *
def main(): 
    n, m, q = MII()
    
    path = [[] for _ in range(n)]
    indeg = [0] * n
    
    for _ in range(m):
        u, v, t, r = MII()
        u -= 1
        v -= 1
        path[u].append((v, t, r))
        indeg[v] += 1
    
    inf = 10 ** 16
    best_result = [[inf] * (2 * n) for _ in range(n)]
    
    best_result[0][n] = 0
    
    stk = [i for i in range(n) if indeg[i] == 0]
    while stk:
        u = stk.pop()
        
        for v, t, r in path[u]:
            for i in range(2 * n):
                if best_result[u][i] < inf:
                    best_result[v][i + r] = fmin(best_result[v][i + r], best_result[u][i] + t)
            
            indeg[v] -= 1
            if indeg[v] == 0:
                stk.append(v)
    
    total_lines = []
    
    for i in range(n):
        lines = []
        for j in range(2 * n - 1, -1, -1):
            k = j - n
            b = best_result[i][j]
            if b < inf:
                while len(lines) >= 2:
                    k1, b1 = lines[-2]
                    k2, b2 = lines[-1]
                    if (k1 - k) * (b2 - b) >= (k2 - k) * (b1 - b): lines.pop()
                    else: break
                lines.append((k, b))
        total_lines.append(lines)
    
    def solve(x, timestamp):
        left, right = 0, len(total_lines[x]) - 1
        
        while left < right:
            mid = (left + right) // 2
            k1, b1 = total_lines[x][mid]
            k2, b2 = total_lines[x][mid + 1]
            if k1 * timestamp + b1 <= k2 * timestamp + b2: right = mid
            else: left = mid + 1
        
        k, b = total_lines[x][left]
        return k * timestamp + b
    
    outs = []
    
    for _ in range(q):
        l, r, x = MII()
        x -= 1
        
        if len(total_lines[x]) == 0:
            outs.append('sorry')
        else:
            outs.append(str(fmin(solve(x, l), solve(x, r))))
    
    print('\n'.join(outs))