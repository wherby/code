# https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95b94/0000000000cad086
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

# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]



def resolve():
    M,R,N= tuple(list(map(lambda x: int(x),input().split())))
    ls = list(map(lambda x: int(x),input().split()))
    lst = 0
    idx = 0
    cnt = 0 
    while idx < N:
        #print(lst,cnt)
        if ls[idx]-R >lst:
            return "IMPOSSIBLE"
        while idx<N-1 and ls[idx+1]-R <=lst:
            idx +=1
        if lst >=M:
            break
        cnt +=1
        #print(ls[idx],idx,lst,ls[idx]-R)
        
        lst = ls[idx]+R 
        idx +=1
    if lst < M:
        return "IMPOSSIBLE"
    return str(cnt)
    
def op(caseidx):
    ret= resolve()
    print("Case #"+str(caseidx+1)+": " + str(ret))
    

for i in range(int(input())):
    op(i)