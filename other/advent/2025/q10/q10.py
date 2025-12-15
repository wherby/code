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


def parser(line):
    ls = line.split("]")
    target = ls[0][1:]
    ls = ls[1].split("{")
    ops = ls[0].split(" ")
    ops = [a[1:-1] for a in ops if len(a)>0]
    ops = [list(map(int,a.split(","))) for a in ops]
    
    return target,ops

def findMinOps(target,ops):
    acc = 0
    for a in target[::-1]:
        if a == ".":
            acc = acc*2+0 
        else:
            acc = acc*2 +1
    target = acc
    m = len(ops)
    opv = []
    for i in range(m):
        acc = 0 
        for b in ops[i]:
            acc += 1<<b 
        opv.append(acc)
    ret =10**20
    for state in range(1<<m):
        bacc = 0 
        for i in range(m):
            if (1<<i)& state:
                bacc ^= opv[i]
        if bacc == target:
            ret = min(ret,state.bit_count())
    return ret
def solve():
    global ls
    sm = 0 
    for line in ls:
        target,ops= parser(line)
        #print(target,ops,findMinOps(target,ops))
        sm += findMinOps(target,ops)
    print(sm)

    

if FILEDEBUG:
    import sys

    orig_stdout = sys.stdout
    f = open('./.tmp/out2.txt', 'w')
    sys.stdout = f

solve()

if FILEDEBUG:
    sys.stdout = orig_stdout
    f.close()
    