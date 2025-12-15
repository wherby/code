import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input.txt"
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

ops = []
opsM =[]


def parser(line):
    global ops
    ls = line.split("]")
    ls = ls[1].split("{")
    ops = ls[0].split(" ")
    ops = [a[1:-1] for a in ops if len(a)>0]
    ops = [list(map(int,a.split(","))) for a in ops]
    val = ls[1]
    val = val[:-1].split(",")
    val = [int(a) for a in val if len(a) >0]
    
    return val,ops





def verify(idx,state):
    global ops,opsM
    t = state[idx]
    opm = opsM[idx]
    acc = 0
    for opt in opm:
        


def findMinOps(target,ops):
    global opsM
    print(target,ops)
    m = len(target)
    opsM = [[] for _ in range(m)]
    print(m,opsM,ops,target)
    for i,t1 in enumerate(ops):
        for b in t1:
            opsM[b].append(i)
    print(opsM)
    return 0
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
    