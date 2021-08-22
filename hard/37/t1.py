boardRes=[]
class Solution(object):
    def fillOneStep(self,board,col,row,sq,index):
        if index == 81:
            #print(board)
            return board
        i = index //9
        j = index %9
        k = board[i][j]
        if k != ".":
            return self.fillOneStep(board,col,row,sq, index +1)
        else:
            res =[]
            for x in range(9):
                if col[i][x] ==0 and row[j][x] ==0 and sq[i//3 *3 + j //3][x] ==0:
                    board[i][j] = str(x+1)
                    #print(board[i][j],x)
                    col[i][x] =1
                    row[j][x] =1
                    sq[i//3 *3 + j //3][x] =1
                    res1= self.fillOneStep(board,col,row,sq,index +1)
                    if len(res1) >0:
                        return board
                    board[i][j] ="."
                    col[i][x] =0
                    row[j][x] =0
                    sq[i//3 *3 + j //3][x] =0  
        return res
                        
            
                 


    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        col  = [[0]*9 for i in range(9)]
        row = [[0]*9 for i in range(9)]
        sq = [[0]*9 for i in range(9)]
        for i in range(9):
            for j in range(9):
                k = board[i][j]
                if k != ".":
                    k = int(k)
                    col[i][k-1] =1
                    row[j][k-1] =1
                    m = i //3
                    n = j //3
                    sq[m*3 + n][k-1] =1
        self.fillOneStep(board,col ,row,sq ,0)

        





board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

Solution().solveSudoku(board)
print(board)