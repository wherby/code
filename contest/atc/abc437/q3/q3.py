
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
# filename = "input/warm_up_input.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin


FILEDEBUG=False

if FILEDEBUG:
    import sys

    orig_stdout = sys.stdout
    f = open('./out.txt', 'w')
    sys.stdout = f


def resolve():
    
    N = int(input())
    ls =[]
    sm = 0
    for i in range(N):
        w,p = list(map(lambda x: int(x),input().split()))
        ls.append((p+w,w,p))
        sm += p
    ls.sort()
    acc = 0
    cnt =0 
    #print(ls,sm)
    for _,w,p in ls:
        acc += w 
        sm -= p
        if acc > sm:
            return cnt 
        #print(w,p, sm, cnt)
        cnt +=1 
    #return 0 

def op(caseidx):
    cnt = resolve()
    print(str(cnt))


for i in range(int(input())):
    op(i)