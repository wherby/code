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
from functools import reduce
def solve():

    lss = []
    for tmp in ls:
        lss.append([a for a in tmp.split(" ") if len(a) >0])
    sm = 0
    for l1 in zip(*lss):
        op = l1[-1]
        t2 = l1[:-1]
        t2 = [int(a) for a in t2 ]
        if op == "*":
            sm += reduce(lambda x,y:x*y,t2)
        else:
            sm += reduce(lambda x,y:x+y,t2)
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
    