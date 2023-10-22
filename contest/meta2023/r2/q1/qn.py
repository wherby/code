#https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d0a5c
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/ready_go_part_1_input.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin



def resolve():
    m,n = tuple(map(lambda x: int(x),input().split()))
    g = []
    for i in range(m):
        g.append(input())
    visit ={}
    def dfs(i,j):
        seeds=set()
        cand =[(i,j)]
        while cand:
            tmp = []
            #print(cand)
            for a,b in cand:
                if (a,b) not in visit:
                    visit[(a,b)] =1
                    for x,y in (a+1,b),(a-1,b),(a,b+1),(a,b-1):
                        if 0<=x<m and 0<=y<n:
                            if g[x][y]== "." :
                                seeds.add((x,y))
                            elif g[x][y] == "W":
                                tmp.append((x,y))
                            else:
                                pass
            cand=tmp
        return len(seeds)
        
    for i in range(m):
        for j in range(n):
            if (i,j) not in visit and g[i][j] =="W":
                re= dfs(i,j)
                #print(re)
                if re == 1:
                    return "YES"
    return "NO"

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)