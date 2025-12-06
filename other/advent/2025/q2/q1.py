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


def getSame(a,b):
    toLen = len(str(b))//2
    ret = 0
    for i in range(1, 10**toLen):
        ii = str(i)+str(i)
        ii  = int(ii)
        if a<=ii<=b:
            ret += ii 
    return ret

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
    