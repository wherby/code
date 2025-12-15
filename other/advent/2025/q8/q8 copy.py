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


class DSU:
    def __init__(self,N):
        self.p  = list(range(N))
        self.rank = [1]*N
    
    def find(self,x):
        if self.p[x] != x:
            self.p[x] =self.find(self.p[x])
        return self.p[x]
    
    def union(self,x,y):
        xr = self.find(x)
        yr = self.find(y)
        if xr == yr:
            return False
        if self.rank[xr] <self.rank[yr]:
            xr,yr =yr,xr
        self.p[yr] = xr
        self.rank[xr] += self.rank[yr]
        return True
from heapq import heapify,heappop,heappush 
from collections import defaultdict,deque
def solve():
    global ls
    ls = [list(map(int,a.split(","))) for a in ls]
    #print(ls)
    n = len(ls)
    dsu = DSU(n)
    def dis(i,j):
        x1,y1,z1 = ls[i]
        x2,y2,z2 = ls[j]
        return (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2
    st = []
    for i in range(n):
        for j in range(i):
            t = dis(i,j)
            st.append((t,i,j))
    heapify(st)
    while st:
        _,i,j = heappop(st)
        dsu.union(i,j)
        if dsu.rank[dsu.find(i)] == n:
            print(ls[i][0]*ls[j][0])
            break

if FILEDEBUG:
    import sys

    orig_stdout = sys.stdout
    f = open('./.tmp/out2.txt', 'w')
    sys.stdout = f

solve()

if FILEDEBUG:
    sys.stdout = orig_stdout
    f.close()
    