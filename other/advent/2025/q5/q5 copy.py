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
from bisect import bisect_right,insort_left,bisect_left
def solve():
    #print(ls)
    rg =[] 
    sd = []
    for a in ls :
        if len(a) ==0:continue
        if a.find("-")>=0:
            t1 = a.split("-")
            t1 = [int(a) for a in t1]
            rg.append(t1)
        else:
            sd.append(int(a))
    rgm = []
    rg.sort()
    fromV = 0 
    toV = -1
    for a,b in rg:
        if a > toV:
            rgm.append([fromV,toV])
            fromV = a 
            toV = b 
        else:
            toV = max(toV,b)
    rgm.append([fromV,toV])
    cnt = 0
    for a,b in rgm:
        cnt += b-a+1
        #print(cnt)
    #print(rgm)
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
    