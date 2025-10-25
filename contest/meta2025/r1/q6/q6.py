
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
filename = "input/crash_course_input.txt"
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
    isG = False
    N, = list(map(lambda x: int(x),input().split()))
    ls =input().split()[0]
    a,b =0,0
    state = 0
    for i in range(N):
        if ls[i] == "A":
            if state <0:
                state = 0
            state +=1
        else:
            state -=1
    return "Alice" if state>0 else "Bob"

 # AAABABBBBBAAAABBAAABB   
    

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))


for i in range(int(input())):
    op(i)