
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
    isG = False
    N,K = list(map(lambda x: int(x),input().split()))
    ls =[]
    for i in range(N):
        inp = int(input())
        ls.append(inp)
    mn = min(ls)
    if K >= mn*(2* max((N-1),1)-1):
        isG = True
    if isG:
        return "YES"
    else:
        return "NO"

def op(caseidx):
    cnt = resolve()
    print(str(cnt))


for i in range(int(input())):
    op(i)