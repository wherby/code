
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

from bisect import bisect_right,insort_left,bisect_left
mod = 998244353
def resolve():

    N,M = list(map(lambda x: int(x),input().split()))
    ls =[]
    for _ in range(2):
        ls.append(list(map(lambda x: int(x),input().split())))
    pre = [0]
    ls[0].sort()
    for a in ls[0]:
        pre.append(pre[-1] +a)
    acc = 0
    for b in ls[1]:
        k = bisect_right(ls[0],b)
        acc += b *k - pre[k] + (pre[-1] -pre[k]) - b *(N-k)
    return acc%mod

def op(caseidx):
    cnt = resolve()
    print(str(cnt))

op(1)
# for i in range(int(input())):
#     op(i)