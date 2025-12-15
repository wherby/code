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
from functools import cache
def solve():
    global ls
    m, n = len(ls) ,len(ls[0])
    cand = []
    for i in range(n):
        if ls[0][i] == "S":
            cand= [i]
    @cache
    def dfs(idx,a):
        if a <0 or a >=n:
            return 0
        if idx == m:
            return 1 
        if ls[idx][a] =="^":
            return dfs(idx+1,a-1) +dfs(idx+1,a+1)
        else:
            return dfs(idx+1,a)
    cnt = dfs(1,cand[0])

    print(cnt)
        
    

if FILEDEBUG:
    import sys

    orig_stdout = sys.stdout
    f = open('./.tmp/out2.txt', 'w')
    sys.stdout = f

solve()

if FILEDEBUG:
    sys.stdout = orig_stdout
    f.close()
    