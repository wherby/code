# https://leetcode.cn/contest/weekly-contest-347/problems/maximum-strictly-increasing-cells-in-a-matrix/
# https://leetcode.cn/circle/discuss/5eR2p8/
# 数据结构优化DP
from typing import List, Tuple, Optional
from collections import defaultdict,deque

class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m,n = len(mat),len(mat[0])
        dic = defaultdict(list)
        for i in range(m):
            for j in range(n):
                dic[mat[i][j]].append((i,j))
        col,row = [0]*m,[0]*n
        for k in sorted(dic.keys()):
            ps = dic[k]
            mx = [0] * len(ps)
            for idx,(px,py) in enumerate(ps): ##对相同值的处理需要先求出各个点的最大值再更新
                tk = max(col[px] +1 ,row[py] +1)
                mx[idx] = tk
            for idx,(px,py) in enumerate(ps):
                col[px] = max(col[px],mx[idx])
                row[py] = max(row[py],mx[idx])
        return max(max(col),max(row))
        





re =Solution().maxIncreasingCells(mat = [[3,1,6],[-9,5,7]])
print(re)