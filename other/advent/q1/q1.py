import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin


def solve():
    ls1,ls2 =[],[]
    for _ in range(1000):
        t1 = list(map(lambda x: int(x),input().split()))
        ls1.append(t1[0])
        ls2.append(t1[1])
    ls1.sort()
    ls2.sort()
    ans = 0 
    from collections import Counter
    c =Counter(ls2)
    for a in ls1:
        ans += a*c[a]
    print(ans)
    


solve()