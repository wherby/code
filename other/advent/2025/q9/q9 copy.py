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



def solve():
    global ls
    ls =[list(map(int,a.split(","))) for a in ls]
    ls.sort()
    vs= set()
    for x,y in ls:
        vs.add(x)
        vs.add(y)
    vs= list(vs)
    vs.sort()
    dic = {}
    for i,v in enumerate(vs,0):
        dic[v] = i 
    N = len(vs)+2
    arr = [[0]*N for _ in range(N)]
    for x,y in ls:
        arr[dic[x]][dic[y]] =1
    n = len(ls) 
    lss = [[] for _ in range(N)]
    for i in range(0,n,2):
        a,b  = ls[i][1],ls[i+1][1]
        lss[dic[ls[i][0]]].append([dic[a],dic[b]])
    # print(len(ls))
    print(lss)
    print(set([len(a) for a in lss]))
    # print(dic)
    #print(arr)
    a = b = -1
    for i in range(N):
        if a != b:
            for j in range(a,b+1):
                #print(a,b,i)
                arr[i][j] = 1
        if len(lss[i]) ==1:
            #print(lss[i])
            a1,b1= lss[i][0]
            if a == -1 and b == -1:
                a,b = a1,b1
            elif a1==a:
                a = b1 
            elif b1 ==a :
                a = a1 
            elif a1 ==b:
                b = b1 
            elif b1 ==b :
                b =a1 
            else:
                print(a,b,a1,b1)
            for j in range(a,b+1):
                arr[i][j] =1 
    #         print(a,b,i)
    # print(arr)


    #         for j in range(a,b+1):
    #             arr[i][j] =1 
    presum = Presum2d(arr)
    # n = len(ls)
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
    