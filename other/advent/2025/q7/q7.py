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

def solve():
    global ls
    m, n = len(ls) ,len(ls[0])
    cand = []
    for i in range(n):
        if ls[0][i] == "S":
            cand= [i]
    cnt = 0
    for i in range(1,m):
        tmp = set([])
        for b in cand:
            if ls[i][b] == "^":
                cnt +=1
                if b +1 < n:
                    tmp.add(b+1)
                if b-1>=0:
                    tmp.add(b-1)
            else:
                tmp.add(b)
        cand = tmp
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
    