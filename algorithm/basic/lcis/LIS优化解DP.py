# https://codeforces.com/gym/105431/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0925/solution/cf105431d.md
# LiS 的DP解法
# L1 从左到右遍历的时候，L2里相同的元素需要从右到左，才能不会有重复的匹配
# 对于l2里的index 用线段树解决 从状态（0,indx-1) 的转移，使得 index 只使用了最多一次 
# algorithm/codeforce/dp/LIS优化解DP.py

import init_setting
from cflibs import *
from lib.segmentTreeWithFuction import segment_tree
def main():
    n, k = MII()
    v1 = LII()
    v2 = LII()
    
    pos = [[] for _ in range(n + 1)]
    
    for i in range(n * k - 1, -1, -1):
        pos[v2[i]].append(i)
    
    fen = segment_tree([0]*(n*k+1),max)
    
    for i in range(n * k):
        for j in pos[v1[i]]:
            fen.update(j + 1, fen.query(0,j) + 1)
    
    print(fen.query(0,n * k))
main()