# https://codeforces.com/gym/104847/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0205/solution/cf104847e.md
# 双参数的最短路径问题
# 因为路径遍历的时候需要权重递增，所以就用权重作为参数排序遍历边
# 而权重有相同的情况，所以每次遍历一批相同权重的边， 使用组内循环找到权重相同的边，然后记录可能的更新，在相同边处理完之后，处理所有更新
# 因为路径是单调递增的，所以在处理更新的时候，不能使用边内更新的结果去更新其他边，所以在遍历所有相等边之后，再更新则不会使得权重值因为同一权重的边访问顺序不一直而不同
# 双参数路径访问问题，利用排序参数控制访问顺序，然后记录cost参数

# 这是一个非常核心的逻辑问题。答案是：必须“打包”在一起更新，不能“按顺序”边走边更新。如果按顺序边走边更新，你会**破坏“严格递增”**的约束，允许程序在同一个版本号内实现“连跳”。
# 1. 为什么“按顺序更新”会出错？假设有两组程序，版本号 $t$ 都是 $10$：程序 A：从 $1 \to 2$（不反转，代价 0）程序 B：从 $2 \to 3$（不反转，代价 0）如果你按顺序边走边更新：
# 处理程序 A：发现 $dis[1]=0$，于是更新 $dis[2]=0$。处理程序 B：此时 $dis[2]$ 已经是 $0$ 了，程序发现 $dis[2]=0$，于是更新 $dis[3]=0$。结果： 你通过版本 $10$ 连跳两次，从 $1 \to 2 \to 3$。
# 错误原因： 题目要求版本必须严格大于。如果你用了版本 $10$ 的程序 A，下一个程序必须是版本 $11, 12...$。在同一个时刻（版本 10），你只能选择走 A 或者走 B，不能“先走 A 再走 B”。2. “打包更新”是如何修正这个问题的？
# 如果你先暂存 updates，处理完所有 $t=10$ 的边后再更新：处理程序 A：看到 $dis[1]=0$，记录 updates.append((2, 0))。处理程序 B：看到 旧的 $dis[2]=\infty$，所以它不会产生任何有效的更新建议。
# 统一更新： 把 $dis[2]$ 设为 $0$。结果： 在这一轮（版本 10）结束时，只有节点 $2$ 被点亮。节点 $3$ 必须等到下一个比 10 更大的版本出现时，才能从节点 $2$ 转移过去。3. 什么时候“按顺序”和“打包”是一样的？
# 只有当图中没有连续的边拥有相同的版本号时，两者的结果才一样。但在算法竞赛或实际工程中，我们必须考虑到“最坏情况”——即大量边共享同一个版本号。总结打包更新（你的代码做法）：代表“这一秒内所有事同时发生，你只能基于前一秒的状态做决定”。
# 这符合“严格递增”的要求。按顺序更新：代表“这件事发生后，下一件事立刻就能利用它的结果”，这变成了“大于等于”的逻辑。
# 这就是为什么你在代码里写那个 while npt < m and ws[st_range[npt]] == ws[st_range[pt]] 的逻辑至关重要的原因。它守护了“严格递增”这条底线。你现在理解为什么那个“临时列表”是这道题的灵魂了吗？




import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    inf = 10 ** 9
    
    for _ in range(t):
        n, m = MII()
        us = []
        vs = []
        ws = []
        
        for _ in range(m):
            u, v, w = GMI()
            us.append(u)
            vs.append(v)
            ws.append(w)
        
        st_range = sorted(range(m), key=lambda x: ws[x])
        dis = [inf] * n
        dis[0] = 0
        
        pt = 0
        while pt < m:
            npt = pt
            while npt < m and ws[st_range[npt]] == ws[st_range[pt]]:
                npt += 1
            
            updates = []
            for i in range(pt, npt):
                u = us[st_range[i]]
                v = vs[st_range[i]]
                updates.append((u, dis[v] + 1))
                updates.append((v, dis[u]))
            
            for u, d in updates:
                dis[u] = fmin(dis[u], d)
            
            pt = npt
        
        outs.append(dis[-1] if dis[-1] < inf else -1)
    
    print('\n'.join(map(str, outs)))