# https://codeforces.com/problemset/problem/1510/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0703/solution/cf1510g.md
# 求一颗树上访问K个节点的最短路径，是从最长路径上选择一个点M，然后在这个点到根的路径遍历一次，其他点遍历两次这样就会获得最短路径
# 如何确定哪些边是一次，哪些边是两次？ 在dfs里的遍历是往下遍历，就是两次，在外面从M到树根的遍历就是1次，而且用cnt控制达到k个点的时候就不会往下遍历

import sys
sys.path.append("..")
from cflibs.cflibs import *
def main():
    t = II()
    outs = []

    for _ in range(t):
        n, k = MII()
        parent = [-1] + LGMI()
        path = [[] for _ in range(n)]
        
        depth = [0] * n
        for i in range(1, n):
            depth[i] = depth[parent[i]] + 1
            path[parent[i]].append(i)
        
        cur = 0
        for i in range(n):
            if depth[i] < k and depth[i] > depth[cur]:
                cur = i
        
        cnt = depth[cur] + 1
        ans = []
        vis = [0] * n
        
        def dfs(i):
            nonlocal cnt
            vis[i] = 1
            ans.append(i)
            for j in path[i]:
                if not vis[j] and cnt < k:
                    cnt += 1
                    dfs(j)
                    ans.append(i)
        
        while cur >= 0:
            dfs(cur)
            cur = parent[cur]
        
        ans.reverse()
        outs.append(str(len(ans) - 1))
        outs.append(' '.join(str(x + 1) for x in ans))

    print('\n'.join(outs))