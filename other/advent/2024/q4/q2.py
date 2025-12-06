import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input.txt"
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
    dirs =[(-1,-1),(1,-1)]

    def isValid(x,y,dx,dy):
        isG = True
        for i in range(-1,2):
            if 0<=dx*i +x < N and 0<=dy*i + y<N:
                pass 
            else:
                isG = False
        return isG
    cnt =0
    for i in range(N):
        for j in range(N):
            isG = True
            for dir in dirs:
                dx,dy = dir
                isva = isValid(i,j,dx,dy)
                if isva == False:
                    isG = False
                if isva:
                    ret =""
                    for k in range(-1,2):
                        ret += ls[i+k*dx][j+k*dy]
                    if ret =="MAS" or ret == "SAM":
                        pass
                    else:
                        isG =False
            if isG:
                cnt +=1


    return cnt
    


print(solve())