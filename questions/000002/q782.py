
from typing import List, Tuple, Optional


class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        def minMove(board):
            n = len(board)

            rmsk=  0 
            for i in range(n):
                rmsk |= board[0][i] <<i 

            
            rr =((1<<n) -1)  - rmsk

            r0,r1 =0,0
            for i in range(n):
                tr =0 
                for j in range(n):
                    tr |= board[i][j]<<j 
                if tr == rmsk :
                    r0 +=1
                elif tr == rr:
                    r1 +=1
                else:
                    return -1
            if abs(r0-r1) >1:
                return -1
            
            if r0!= r1:
                mv=0 
                #print(r0,r1)
                if r0>r1:
                    for i in range(n):
                        if board[i][0] != (board[0][0] +i) %2:
                            #print(i,board[0][i],board[0])
                            mv +=1
                else:
                    for i in range(n):
                        if board[i][0] != (board[0][0] +1+i) %2:
                            #print(i,board[0][i],board[0],"a")
                            mv +=1
                return mv 
            else:
                mv1,mv2= 0,0
                for i in range(n):
                    if board[0][i] != (board[0][0] +i) %2:
                        mv1 +=1
                    if board[0][i] == (board[0][0] +i) %2:
                        mv2 +=1
                return min(mv1,mv2)
        a = minMove(board)
        b = minMove(list(zip(*board)))
        #print(a,b)
        return (a +b)//2 if a!=-1 and b!=-1 else -1
    
re =Solution().movesToChessboard(board = [[1,1,0],[0,0,1],[0,0,1]])
print(re)