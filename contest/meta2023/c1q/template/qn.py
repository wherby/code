#https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d0a5c
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/second_hands_input.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin


from collections import Counter
def resolve():
    isG = True
    n,k = list(map(lambda x: int(x),input().split()))
    ls =list(map(lambda x: int(x),input().split()))
    if n>2*k:
        isG =False
    c =Counter(ls)
    for _,v in c.items():
        #print(v)
        if v>2:
            isG =False
    if isG:
        return "YES"
    else:
        return "NO"

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)