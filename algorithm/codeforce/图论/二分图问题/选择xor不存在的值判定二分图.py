# https://codeforces.com/gym/102419/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/10/1015/solution/cf102419d.md
# 因为题目需要选择一些点，xor之后不会有边连接重复点
# 选择了相同值的边构建二分图
# 为了找到一个值，使得xor值后能生成不冲突的点，
# 则需要把原来不同值的边取xor,如果没在这些值出现的X就可以是选择值
# 已知 (A,B) 求C使得， AxorC != B => C != A xor B  


import init_setting
from cflibs import *
def main():
    n, m = MII()
    nums = LII()
    vis = [0] * (1 << 20)
    
    path = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v = GMI()
        if nums[u] == nums[v]:
            path[u].append(v)
            path[v].append(u)
        else:
            vis[nums[u] ^ nums[v]] = 1
    
    col = [-1] * n
    
    for i in range(n):
        if col[i] == -1:
            col[i] = 0
            
            stk = [i]
            while stk:
                u = stk.pop()
                
                for v in path[u]:
                    if col[v] == -1:
                        col[v] = col[u] ^ 1
                        stk.append(v)
                    elif col[u] == col[v]:
                        exit(print(-1))
    
    chosen = 1
    while vis[chosen]:
        chosen += 1
    
    print(sum(col), chosen)
    print(*(i + 1 for i in range(n) if col[i]))