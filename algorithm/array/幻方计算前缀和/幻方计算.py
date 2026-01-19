from typing import List, Tuple, Optional

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # 1. 预处理行、列前缀和 (多申请一行一列方便计算)
        row_sum = [[0] * (n + 1) for _ in range(m)]
        col_sum = [[0] * (n) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                row_sum[i][j+1] = row_sum[i][j] + grid[i][j]
                col_sum[i+1][j] = col_sum[i][j] + grid[i][j]
                
        # 2. 预处理对角线前缀和
        diag1 = [[0] * (n + 1) for _ in range(m + 1)] # 主对角线 \
        diag2 = [[0] * (n + 1) for _ in range(m + 1)] # 副对角线 /
        for i in range(m):
            for j in range(n):
                diag1[i+1][j+1] = diag1[i][j] + grid[i][j]
                diag2[i+1][j] = diag2[i][j+1] + grid[i][j]

        def check(r, c, k):
            # 获取目标和（以第一行为基准）
            target = row_sum[r][c+k] - row_sum[r][c]
            
            # 校验每一行
            for i in range(r + 1, r + k):
                if row_sum[i][c+k] - row_sum[i][c] != target: return False
            # 校验每一列
            for j in range(c, c + k):
                if col_sum[r+k][j] - col_sum[r][j] != target: return False
            # 校验对角线 \
            if diag1[r+k][c+k] - diag1[r][c] != target: return False
            # 校验对角线 /
            if diag2[r+k][c] - diag2[r][c+k] != target: return False
            
            return True

        # 从最大可能的长度开始搜索，找到即可返回
        for k in range(min(m, n), 1, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if check(i, j, k):
                        return k
        return 1