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
    line = line.split(":")
    a = line[0].strip()
    tols = line[1].split(" ")
    tols = [a.strip() for a in tols if len(a)>0]
    return a,tols
from functools import cache
def solve():
    global ls 
    #print(ls)
    g= {}
    for line in ls:
        a,tols = parser(line)
        g[a]= tols
    
    @cache 
    def dfs(a):
        if len(g[a]) ==1 and g[a][0] == "out":
            return 1 
        ret = 0
        for b in g[a]:
            ret += dfs(b)
        return ret 
    res= dfs("you")
    print(res)

    

if FILEDEBUG:
    import sys

    orig_stdout = sys.stdout
    f = open('./.tmp/out2.txt', 'w')
    sys.stdout = f

solve()

if FILEDEBUG:
    sys.stdout = orig_stdout
    f.close()
    