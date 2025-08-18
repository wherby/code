# https://codeforces.com/problemset/problem/1913/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0816/solution/cf1913e.md
# 为什么0变成1的cost是2？
# cur 表示以前的1，最终的1的数量是 sum(nums1)
# cur - (1->0) + (0->1) == sum(nums1)
#  (1->0) = cur + (0->1) - sum(num1)
#  (1->0) + (0->1) = cur + 2*(0->1) -sum(num1)
#  cost= (1->0) + (0->1)  = cur + 2*(0->1) -sum(num1) 
# 
# algorithm/graph/flow/mincost/费用流解决矩阵变换问题.py 这里有直接求的解法

import init_setting
from lib.cflibs import *
from lib.mincostflow import *
def main():
    n, m = MII()
    grid = [LII() for _ in range(n)]
    
    nums1 = LII()
    nums2 = LII()
    
    mcf = MCFGraph(n + m + 2)
    
    src = n + m
    dst = n + m + 1
    
    cur = sum(sum(x) for x in grid)
    
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                mcf.add_edge(i, j + n, 1, 0)
            else:
                mcf.add_edge(i, j + n, 1, 2)
    
    for i in range(n):
        mcf.add_edge(src, i, nums1[i], 0)
    
    for i in range(m):
        mcf.add_edge(n + i, dst, nums2[i], 0)
    
    mf, mc = mcf.flow(src, dst)
    
    if mf == sum(nums1) == sum(nums2):
        print(mc + (cur - sum(nums1)))
    else:
        print(-1)

main()