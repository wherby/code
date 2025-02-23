import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin




def solve():
    ls = [input()]
    N = len(ls[0])
    for _ in range(1,N):
        ls.append(input())
    dir= [(1,0),(0,1),(1,1),(-1,1)]

    def isValid(x,y,dx,dy):
        isG = True
        for i in range(4):
            if 0<=dx*i +x < N and 0<=dy*i + y<N:
                pass 
            else:
                isG = False
        return isG
    
    cnt =0
    for i in range(N):
        for j in range(N):
            for dx,dy in dir:
                if isValid(i,j,dx,dy):
                    ret = ""
                    for k in range(4):
                        ret+=ls[i+k*dx][j+k*dy]
                    if ret == "XMAS" or ret == "SAMX":
                        cnt +=1
    return cnt
    


print(solve())