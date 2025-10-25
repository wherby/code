
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
filename = "input/snake_scales_chapter_2_input.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin


FILEDEBUG=True

if FILEDEBUG:
    import sys

    orig_stdout = sys.stdout
    f = open('./out.txt', 'w')
    sys.stdout = f



from heapq import heapify,heappop,heappush 
def resolve():
    ret = 0
    N, = list(map(lambda x: int(x),input().split()))
    ls =list(map(lambda x: int(x),input().split()))
    g = [[] for _ in range(N+1)]
    for i in range(N):
        g[i+1].append((0,ls[i]))
        if i >0:
            g[i+1].append((i,abs(ls[i] - ls[i-1])))
        if i < N-1:
            g[i+1].append((i+2,abs(ls[i]-ls[i+1])))
    visit={}
    st= []
    for i in range(N):
        heappush(st,(ls[i],i+1))
    while st:
        cost,pt = heappop(st)
        if pt not in visit:
            ret = max(ret,cost)
            visit[pt] =1
            for b,cst in g[pt]:
                heappush(st,(cst,b))
    return ret

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))


for i in range(int(input())):
    op(i)