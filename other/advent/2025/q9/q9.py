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
    ls =[list(map(int,a.split(","))) for a in ls]
    ls.sort()
    n = len(ls)
    mx = 0
    for i in range(n):
        x1,y1 = ls[i]
        for j in range(n):
            x2,y2= ls[j]
            t1 =(1+abs(x1-x2))*(1+abs(y1-y2))
            mx= max(mx,t1)
    print(mx)
    

if FILEDEBUG:
    import sys

    orig_stdout = sys.stdout
    f = open('./.tmp/out2.txt', 'w')
    sys.stdout = f

solve()

if FILEDEBUG:
    sys.stdout = orig_stdout
    f.close()

