import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
f=open(filename,'r')
FILEDEBUG=False
from heapq import heapify,heappop,heappush 
from collections import defaultdict,deque
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin


mp =[]
a = input()
dic =defaultdict(lambda : 10**10)
idx =0
while len(a)>1:
    ls = a.split(",")
    ls= [int(a) for a in ls]
    #ls= ls[::-1]
    mp.append(ls)
    
    a = input()


def solve(kidx):
    N=70
    

    for i,(x,y) in enumerate(mp):
        if i <kidx:
            dic[(x,y)] =1
    #print(kidx,mp[kidx-1])
    dq = deque([(0,0,0)])
    visit = defaultdict(lambda :10**10)
    #print(dic)
    acc =0
    while dq:
        # acc +=1 
        # if acc >1000:
        #     break
        c,x,y = dq.popleft()
        if visit[(x,y)] <=c:continue
        visit[(x,y)] =c
        #print(x,y,c,visit)
        if x == N and y==N:
            #print(c)
            return True
        for dx,dy in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
            if  (dx,dy) not in dic and 0<=dx<=N and 0<=dy<= N and c+1<visit[(dx,dy)]:
                dq.append((c+1,dx,dy))
                #print(x,y,dx,dy)
    return False


    

if FILEDEBUG:
    import sys

    orig_stdout = sys.stdout
    f = open('./.tmp/out2.txt', 'w')
    sys.stdout = f

isG = True
for i in range(3450):
    re =solve(i)
    if re ==False and isG:
        print(i,mp[i-1])
        print(re)
        isG =False

if FILEDEBUG:
    sys.stdout = orig_stdout
    f.close()
    