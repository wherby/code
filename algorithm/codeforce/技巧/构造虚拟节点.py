# https://codeforces.com/problemset/problem/274/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/06/0613/solution/cf274d.md
# 如果有重复节点的时候，构造拓扑图的时候会出现N**2复杂度，这时候把相同值的节点构造成虚拟节点，这样就只有N的复杂度
# pt 虚拟节点，同一行的值压缩为同一节点
#Tips#节点压缩

# 拓扑排序逻辑节点
# 因为需要求列的顺序，所以把所有同列的点都连在列的虚拟节点上，
# 上一逻辑节点 -》当前列节点
# 当前列节点 ->当前逻辑节点
# 所以所有的前逻辑节点被访问，才能解锁下一层的列节点，上一层的列节点解锁了，就可以解锁当层的逻辑节点
# 所以当前列的所有的列节点和逻辑节点都被访问，就会解锁下一列的逻辑列节点和列节点，完成拓扑遍历

import init_setting
from cflibs import *
def main():
    n, m = MII()
    grid = [LII() for _ in range(n)]

    path = [[] for _ in range(m + n * m)]
    indeg = [0] * (m + n * m)
    pt = m

    for i in range(n):
        idxs = [j for j in range(m) if grid[i][j] != -1]
        idxs.sort(key=lambda x: grid[i][x])
        
        l, r = 0, 0
        last_node = -1
        
        for j in range(1, len(idxs)):
            if grid[i][idxs[j]] == grid[i][idxs[j - 1]]:
                r = j
            else:
                if last_node != -1:
                    for idx in range(l, r + 1):
                        path[last_node].append(idxs[idx])
                        indeg[idxs[idx]] += 1
                
                for idx in range(l, r + 1):
                    path[idxs[idx]].append(pt)
                    indeg[pt] += 1

                last_node = pt
                pt += 1
                l = r = j
        
        if last_node!= -1:
            for idx in range(l, r + 1):
                path[last_node].append(idxs[idx])
                indeg[idxs[idx]] += 1

    stk = [i for i in range(m + n * m) if indeg[i] == 0]
    ans = []

    while stk:
        u = stk.pop()
        if u < m:
            ans.append(u)
        for v in path[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                stk.append(v)

    if len(ans) == m: print(' '.join(str(x + 1) for x in ans))
    else: print(-1)