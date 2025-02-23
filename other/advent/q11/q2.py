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
from collections import Counter

def solve():
    ls= input()
    ls = list(map(int, ls.split(" ")))
    c = Counter(ls)
    for _ in range(75):
        c1 = Counter()
        for k,v in c.items():
            if k ==0:
                c1[1] += v
            elif len(str(k)) %2 ==0:
                s = str(k)
                m = len(s)
                c1[int(s[:m//2])] += v
                c1[int(s[m//2:])] += v
            else:
                c1[k*2024] +=v
        c = c1
    print(sum(c.values()))



solve()