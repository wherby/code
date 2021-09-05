#https://www.hackerrank.com/contests/world-codesprint-12/challenges/red-knights-shortest-path/problem
#!/bin/python

import sys

moves = [[-1,-2],[1,-2],[2,0],[1,2],[-1,2],[-2,0]]
dic1 = {(-2,0):"L", (2,0):"R",(-1,-2):"UL", (1,-2):"UR",(-1,2):"LL",(1,2):"LR"
    
}


def bfs(point,visited,n):
    global moves
    x,y,path = point
    re = []

    for move in moves:
        x1 = x + move[0]
        y1 = y + move[1]
        if x1 >=0 and x1 < n and y1 >=0 and y1 <n:
            if visited[x1][y1] == 0:
                visited[x1][y1] =1
                path1 = list(path)
                path1.append(move)
                re.append([x1,y1,path1])
    return re

def printRes(ls):
    global dic1
    print len(ls)
    re=""
    for m in ls:
        t = dic1[(m[0],m[1])]
        re = re + t + " "
    print re.strip() 


def printShortestPath(n, i_start, j_start, i_end, j_end):
    #  Print the distance along with the sequence of moves.
    visited = [[0] * n for _ in range(n)]
    stack = [[j_start,i_start,[]]]
    while stack:
        p1 = stack.pop(0)
        #print p1
        if p1[1] == i_end and p1[0] ==j_end:
            printRes( p1[2])
            return
        re = bfs(p1,visited,n)
        stack.extend(re)
    print "Impossible"

    



printShortestPath(7,6,6,0,1)

# if __name__ == "__main__":
#     n = int(raw_input().strip())
#     i_start, j_start, i_end, j_end = raw_input().strip().split(' ')
#     i_start, j_start, i_end, j_end = [int(i_start), int(j_start), int(i_end), int(j_end)]
#     printShortestPath(n, i_start, j_start, i_end, j_end)
