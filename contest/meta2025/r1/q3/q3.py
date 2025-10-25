
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
filename = "input/final_product_chapter_1_input.txt"
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


def resolve():
    N,A,B = list(map(lambda x: int(x),input().split()))
    ret = [1]*N*2
    ret[-1] = B
    ret = [str(a) for a in ret]
    return " ".join(ret)

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+cnt)


for i in range(int(input())):
    op(i)