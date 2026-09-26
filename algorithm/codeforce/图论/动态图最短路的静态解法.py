# https://codeforces.com/gym/106682/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0904/solution/cf106682f.md
# 按照题目的意思，求函数的最小值的时候，由于边权是单调递增，所以边权取极值的时候为最小值，且前面为0，后面为1
# 这时就可以暴力枚举边权0,1 的分界点
# 然后使用01BFS 双端队列进行求距离和函数值，这里使用了静态双向预留数组，虽然改变l的值的时候会重复访问某一点，但是松弛带来的重复冗余是常数
# l -= 1 抢占队头不是冗余，而是严格的 Dijkstra 贪心：
# 当通过 0 权边松弛点 $v$ 时，将 $v$ 压入队头（l -= 1）并在下一轮立刻弹出 $v$，这本质上是 Dijkstra 算法中对 0 权边的优先扩展。虽然指针 $l$ 减小了，但由于有 if dis[v] > nd 的严格关卡，每个点只会被有效松弛有限次，因此这部分时间完全被包含在了线性的 $O(N + M)$ 复杂度之内。#
# algorithm/codeforce/docs/图论/动态图01BFS最短路径维护.md


import init_setting
from cflibs import *
def main():
    n, m = MII()
    
    us = []
    vs = []
    
    path = [[] for _ in range(n)]
    
    for eid in range(m):
        u, v = GMI()
        us.append(u)
        vs.append(v)
        path[u].append(eid)
        path[v].append(eid)
    
    dis = [n] * n
    que = [0] * (4 * n)
    ans = [n] * m
    
    for i in range(m):
        l = r = 2 * n
    
        dis[0] = 0
        que[l] = 0
        
        while l <= r:
            u = que[l]
            l += 1
            
            for eid in path[u]:
                v = us[eid] + vs[eid] - u
                if eid >= i: nd = dis[u] + 1
                else: nd = dis[u]
                
                if dis[v] > nd:
                    if eid >= i:
                        dis[v] = nd
                        r += 1
                        que[r] = v
                    else:
                        dis[v] = nd
                        l -= 1
                        que[l] = v
    
        for j in range(i, m):
            ans[j] = fmin(ans[j], dis[n - 1] / (j - i + 1))
    
        for u in range(n):
            dis[u] = n
    
    print('\n'.join(f'{x:.9f}' for x in ans))