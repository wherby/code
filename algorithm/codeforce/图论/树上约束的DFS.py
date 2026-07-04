# https://codeforces.com/gym/106020/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0629/solution/cf106020a.md
# 贪心处理每个树区域
# 在内层循环的时候，把已经可以确定的邻居加入队列的方法，在图的处理上更好
# 在本题中不用内层循环的处理其实也可以，因为遍历最近邻居就好了，最近邻居的遍历次数为 2*(n-1)，但是如果有循环限制等等，就需要内层队列了
# 图论中，这种“一旦确定就立刻入队扩散”的思想，就是经典的拓扑排序（Topological Sort）、染色法判定二分图以及约束满足问题（CSP）中的弧相容（Arc Consistency, AC-3）算法的核心。
# algorithm/codeforce/docs/弧相容问题拓扑排序.md

import init_setting
from cflibs import *
def main():
    n = II()
    path = [[] for _ in range(n)]
    
    for _ in range(n - 1):
        u, v = GMI()
        path[u].append(v)
        path[v].append(u)
    
    possible = [[1] * n for _ in range(3)]
    ans = [-1] * n
    
    for i in range(n):
        if ans[i] == -1:
            chosen = 0
            for j in range(3):
                if possible[j][i] == 1:
                    chosen = j
                    break
            
            for j in range(3):
                if j != chosen:
                    possible[j][i] = 0
            
            ans[i] = chosen
            que = [i]
            
            for u in que:
                for v in path[u]:
                    if ans[v] == -1:
                        possible[ans[u]][v] = 0
                        
                        c = 0
                        for j in range(3):
                            c += possible[j][v]
                        
                        if c == 1:
                            for j in range(3):
                                if possible[j][v]:
                                    ans[v] = j
                            que.append(v)
    
    print(''.join(chr(ord('a') + x) for x in ans))