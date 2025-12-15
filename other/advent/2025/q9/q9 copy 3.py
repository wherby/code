import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
f=open(filename,'r')
FILEDEBUG=False

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin



ls = []
try:
    with open(filename, 'r') as file:
        for line in file:
            ls.append(line.strip())
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")


class Presum2d:
    def __init__(self,arr):
        m,n = len(arr),len(arr[0])
        self.pre = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                #print(i,j,m,n)
                self.pre[i+1][j+1] = self.pre[i][j+1] + self.pre[i+1][j] -self.pre[i][j] + arr[i][j]
    
    def query(self,x1,y1,x2,y2):
        a = self.pre[x2+1][y1]
        b = self.pre[x1][y2+1]
        c = self.pre[x1][y1]
        return self.pre[x2+1][y2+1] -a -b +c

from itertools import pairwise

def solve():
    global ls
    ls =[list(map(int,a.split(","))) for a in ls]
    vs= set()
    for x,y in ls:
        vs.add(x)
        vs.add(y)
    vs= list(vs)
    vs.sort()
    dic = {}
    for i,v in enumerate(vs):
        dic[v] = i*2 
    N = len(vs)*2+2
    arr = [[0]*N for _ in range(N)]
    ls.append(ls[0])
    for a,b in pairwise(ls):
        #print(a,b)
        x1,y1 = a 
        x2,y2 = b 
        x1,y1 = dic[x1],dic[y1]
        x2,y2 = dic[x2],dic[y2]
        if x1 == x2:
            miny,maxy = min(y1,y2),max(y1,y2)
            for j in range(miny,maxy+1):
                arr[x1][j] = 1 
        else:
            minx,maxx = min(x1,x2),max(x1,x2)
            for j in range(minx,maxx+1):
                arr[j][y1] = 1 

    # for i in range(N):
    #     left = N 
    #     right = 0 
    #     for j in range(N):
    #         if arr[i][j] == 1:
    #             left = min(left,j)
    #             right = max(right,j)
    #     for j in range(left,right+1):
    #         arr[i][j] =1 


    seed =[]
    vist={}
    def bfs(seed,k):
        while seed:
            x,y = seed.pop()
            arr[x][y] =k 
            for dx,dy in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                if (dx,dy) not in vist and 0<=dx<N and 0<=dy<N and arr[dx][dy] ==0:
                    seed.append((dx,dy))
                    vist[(dx,dy)] =k
    for i in range(N):
        if arr[0][i] == 0:
            seed.append([0,i])
            
        if arr[i][0] == 0:
            seed.append([i,0])
            
        if arr[N-1][i] ==0:
            seed.append([N-1,0])
            
        if arr[i][N-1] ==0:
            seed.append([i,N-1])
             
    
    if len(seed) >0:
        bfs(seed,2)

    
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                arr[i][j] =0 
            elif arr[i][j] ==0:
                arr[i][j] =1
    # for i in range(N):
    #     print(arr[i])
    presum = Presum2d(arr)
    n = len(ls)
    ret = 0
    for i in range(n):
        x1,y1 = ls[i]
        x1idx,y1idx = dic[x1],dic[y1]
        for j in range(i):
            x2,y2 = ls[j]
            x2idx,y2idx = dic[x2],dic[y2]
            mx,my = max(x1idx,x2idx),max(y1idx,y2idx)
            nx,ny = min(x1idx,x2idx),min(y1idx,y2idx)
            if presum.query(nx,ny,mx,my) ==(mx-nx+1)*(my-ny+1):
                ret = max(ret,(abs(x1-x2)+1)*(abs(y1-y2)+1))
                #print(i,j, x1,y1,x2,y2, (abs(x1-x2)+1)*(abs(y1-y2)+1) )
        
    print(ret)

if FILEDEBUG:
    import sys

    orig_stdout = sys.stdout
    f = open('./.tmp/out2.txt', 'w')
    sys.stdout = f

solve()

if FILEDEBUG:
    sys.stdout = orig_stdout
    f.close()
    