# https://codeforces.com/gym/104287/problem/N
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0107/solution/cf104287n.md
# 寻找两条不相交的链最小值的最大值
#  需要两个阶段，第一阶段，解决当前点子树下的最长直径和以当前点为中点的最长链
        # up_dp0 = [0] * n  # up_long[u]: 从u向上的最长链
        # up_dp1 = [0] * n  # up_dia[u]: 去掉子树u后的直径
# 考虑了从上面连接的时候，考虑 父节点收集了从上而来的连接长度，得到了三个以父节点未终点的最长链
        #     v1, v2, v3 = up_dp0[u], 0, 0  # 从节点 u 出发的所有可能链的前三长
        #     w1, w2 = 0, 0                 # 所有子节点子树直径的前两大
# 然后用这三个了链的长度，分情况得到，以当前点作为分割点的 子树最大直径和除去当前子树的最大直径 和更新到当前点V的最长向上路径
        # up_dp0 = [0] * n  # up_long[u]: 从u向上的最长链
        # up_dp1 = [0] * n  # up_dia[u]: 去掉子树u后的直径
# 而其中树上最长和第二长的路径是由 当前点为终点的时候记录的，这两条路径是可能重叠的，但是记录的 dp1 和 up_dp1 则是在每次分割的两个图形的最大直径
# 因为当前访问V的时候得到了 w1,w2 这时单个点最多贡献了一个路径，所以一定能找到和当前子树无关的直径
                    # 考虑兄弟子树的直径
                    # if dp1[v] == w1: 
                    #     up_dp1[v] = fmax(up_dp1[v], w2)  # v是最大直径，用次大
                    # else: 
                    #     up_dp1[v] = fmax(up_dp1[v], w1)  # v不是最大，用最大


import init_setting
from lib.cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        path = [[] for _ in range(n)]
        
        for _ in range(n - 1):
            u, v, w = MII()
            u -= 1
            v -= 1
            path[u].append(w * n + v)
            path[v].append(w * n + u)
        
        parent = [-1] * n
        que = [0]
        
        for u in que:
            for msk in path[u]:
                w, v = divmod(msk, n)
                if parent[u] != v:
                    parent[v] = u
                    que.append(v)
        
        dp0 = [0] * n  # down_long[u]: 从u向下的最长链
        dp1 = [0] * n  # down_dia[u]: 子树u的直径
        
        for u in reversed(que):
            v1, v2 = 0, 0
            
            for msk in path[u]:
                w, v = divmod(msk, n)
                if parent[v] == u:
                    nw = w + dp0[v]
                    if nw > v1: v1, v2 = nw, v1
                    elif nw > v2: v2 = nw
                    dp1[u] = fmax(dp1[u], dp1[v])
            
            dp0[u] = v1
            dp1[u] = fmax(dp1[u], v1 + v2)
        
        up_dp0 = [0] * n  # up_long[u]: 从u向上的最长链
        up_dp1 = [0] * n  # up_dia[u]: 去掉子树u后的直径
        
        for u in que:
            v1, v2, v3 = up_dp0[u], 0, 0  # 从节点 u 出发的所有可能链的前三长
            w1, w2 = 0, 0                 # 所有子节点子树直径的前两大
            
            # 收集u的所有可能链：包括向上链和所有子链
            for msk in path[u]:
                w, v = divmod(msk, n)
                
                if parent[v] == u:
                    nw = w + dp0[v]
                    if nw > v1: v1, v2, v3 = nw, v1, v2
                    elif nw > v2: v2, v3 = nw, v2
                    elif nw > v3: v3 = nw
                    
                    if dp1[v] > w1: w1, w2 = dp1[v], w1
                    elif dp1[v] > w2: w2 = dp1[v]
            
            # 计算每个子节点v的向上信息
            for msk in path[u]:
                w, v = divmod(msk, n)
                
                if parent[v] == u:
                    nw = w + dp0[v]
                    if nw == v1:  # v贡献了v1
                        up_dp0[v] = v2 + w  # 向上链 = 次大链 + w
                        up_dp1[v] = v2 + v3  # 向上直径可能来自两个次大链
                    elif nw == v2:  # v贡献了v2
                        up_dp0[v] = v1 + w  # 向上链 = 最大链 + w
                        up_dp1[v] = v1 + v3  # 向上直径可能来自最大和第三大
                    else:  # v贡献了v3或更小
                        up_dp0[v] = v1 + w  # 向上链 = 最大链 + w
                        up_dp1[v] = v1 + v2  # 向上直径来自最大和次大
    
                    # 考虑兄弟子树的直径
                    if dp1[v] == w1: 
                        up_dp1[v] = fmax(up_dp1[v], w2)  # v是最大直径，用次大
                    else: 
                        up_dp1[v] = fmax(up_dp1[v], w1)  # v不是最大，用最大
        
        outs.append(max(fmin(dp1[i], up_dp1[i]) for i in range(n)))
    
    print('\n'.join(map(str, outs)))

main()