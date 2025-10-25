
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
filename = "input/narrowing_down_input.txt"
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

from collections import defaultdict,deque
def resolve():
    N, = list(map(lambda x: int(x),input().split()))
    ls =list(map(lambda x: int(x),input().split()))
    dic = defaultdict(int)
    dic[0]=1
    cur = 0  
    acc =0
    ret =0
    for i,a in enumerate(ls):
        cur = (i+1)*(i+2) //2
        #print(cur,i)
        acc =acc ^ a 
        ret +=cur - dic[acc]*(dic[acc]+1)//2
        dic[acc]+=1
        
        
    return ret

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))


for i in range(int(input())):
    op(i)