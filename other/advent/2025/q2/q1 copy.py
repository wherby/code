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


def getSameK(a,b,k):
    toLen = len(str(b))//k
    ret = set([])
    for i in range(1, 10**toLen):
        ii = str(i)*k
        ii  = int(ii)
        if a<=ii<=b:
            ret.add(ii)
    return ret

def getSame(a,b):
    blen = len(str(b))
    res = set()
    for k in range(2,blen+1):
        t1 = getSameK(a,b,k)
        res =res | t1 
    return sum(res)

def solve():
    global ls
    ls = ls[0].split(",")
    lss = []
    sm =0
    for a in ls:
        x,y = a.split("-")
        lss.append([int(x),int(y)])
    for a,b in lss:
        sm += getSame(a,b)
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
    