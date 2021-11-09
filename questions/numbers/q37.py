import copy
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        res =[[]]
        def valid(i,j,k):
            for n in range(9):
                if board[i][n] ==k:
                    return False
            for m in range(9):
                if board[m][j] == k:
                    return False
            a = i//3 *3
            b = j //3 *3
            for m in range(3):
                for n in range(3):
                    if board[a+m][b+n] ==k:
                        return False
            return True
        def dfs(i,j):
            if len(res[0]) >0:
                return True
            if i == 9: 
                res[0] = copy.deepcopy(board)
                return True
            if j ==9: return dfs(i+1,0)
            if board[i][j] ==".":
                for k in range(1,10):
                    ks = str(k)
                    if  valid(i,j,ks):
                        board[i][j] =ks
                        if dfs(i,j+1):
                            return True
                        board[i][j] ="."
            else:
                return dfs(i,j+1)
        dfs(0,0)
        #print(res)
        return res[0]
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
re =Solution().solveSudoku(board)
