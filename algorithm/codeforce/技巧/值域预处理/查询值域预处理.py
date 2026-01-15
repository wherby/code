# https://codeforces.com/gym/104294/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0107/solution/cf104287a.md
# 区间查询对的最大最小优化
# 在这个题目中，矩阵中的元素值是固定在0到N之间，为了加速查询效率，可以在值域上看每个当前值，取 K 个对角线长度的时候，能得到最小的范围
# 然后 同理在 saved[i][j] = fmin(saved[i][j], saved[i][j + 1]) 对最小值进行查询DP优化， 条件更宽松的放缩， 因为从 j+1 开始i个位置的最小值可以是 K， 则从j开始 i个位置的最小值一定至少是K,因为 j开始的条件状态包含了 j+1开始的条件状态
# 使得可以在查询的时候直接使用a值作为起始值查询



import init_setting
from cflibs import *

def main(): 
    n, q = MII()
    grid = [LII() for _ in range(n)]
    
    saved = [[n * n + 1] * (n * n + 1) for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i + k >= n or j + k >= n:
                    break
                saved[k][grid[i][j]] = fmin(saved[k][grid[i][j]], grid[i + k][j + k])
    
    for i in range(n):
        for j in range(n * n - 1, -1, -1):
            saved[i][j] = fmin(saved[i][j], saved[i][j + 1])
    
    outs = []
    
    for _ in range(q):
        a, b = MII()
        
        for i in range(n - 1, -1, -1):
            if saved[i][a] <= b:
                outs.append((i + 1) ** 2)
                break
    
    print('\n'.join(map(str, outs)))
main()