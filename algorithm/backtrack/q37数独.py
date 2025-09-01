# https://leetcode.cn/problems/sudoku-solver/solutions/3767438/shu-du-zen-yao-wan-ti-mu-jiu-zen-yao-zuo-ms2q/?envType=daily-question&envId=2025-08-31
from typing import List, Tuple, Optional

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dp =[[0]*9 for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    a = int(board[i][j])
                    dp[0][i] += 1<< a 
                    dp[1][j] += 1<<a 
                    k = i //3 + (j//3)*3 
                    dp[2][k] += 1<<a 
        ret = []
        ms = 0 
        start = 0
        for i in range(9):
            c =len([a for a in board[i] if a != "."])
            #print(c) 
            if c > ms:
                ms = c 
                start = (c-1)*9 
            
        def dfs(idx):
            nonlocal ret
            idx2 = (start+idx)%81
            i,j = idx2%9,idx2//9
            if idx == 81:
                #print("aa")
                ret = [list(a) for a in board]
                return True
            if board[i][j]!= ".":
                return dfs(idx+1)
            for m in range(1,10):
                k = i //3 + (j//3)*3 
                if (dp[0][i] & (1<<m) == 0) and (dp[1][j] &(1<<m) ==0) and (dp[2][k] &(1<<m) ==0):
                    board[i][j] = str(m)
                    dp[0][i] += 1<<m 
                    dp[1][j] += 1<<m 
                    dp[2][k] += 1<<m 
                    if dfs(idx+1):
                        return True
                    board[i][j] = "."
                    dp[0][i] -= 1<<m 
                    dp[1][j] -= 1<<m 
                    dp[2][k] -= 1<<m 
            return False
        dfs(0)
        for i in range(9):
            for j in range(9):
                board[i][j] = ret[i][j]
        print(board)



board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
board = [[".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]]
re =Solution().solveSudoku(board)
print(re)