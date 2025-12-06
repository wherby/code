# https://adventofcode.com/2025/day/6#part2
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
            ls.append(line.rstrip())
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
from functools import reduce
def solve():
    global ls
    mx = max([len(a) for a in ls])+1
    ls = [a + " "*(mx- len(a)) for a in ls]
    m = len(ls)
    tmp = []
    op = ""
    #print(ls)
    sm =0
    for i in range(mx):
        t=""
        for j in range(m-1):
            t+=ls[j][i]
        if ls[m-1][i] !=" ":
            op = ls[m-1][i]
        #print(i,t,ls[m-1][i])
        if len(t.strip()) != 0:
            tmp.append(int(t))
        else:
            if op == "*":
                sm += reduce(lambda x,y:x*y,tmp)
                tmp = []
            else:
                sm += reduce(lambda x,y:x+y,tmp)
                tmp = []
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
    