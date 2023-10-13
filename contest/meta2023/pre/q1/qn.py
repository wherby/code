#https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d0a5c
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/cheeseburger_corollary_1_input.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin



def resolve():
    isG = True
    a,b,c = list(map(lambda x: int(x),input().split()))
    if a + 2*b <c:
        isG =False
    if 2*a + 2*b < c+1:
        isG =False
    #print(a,b,c)
    if isG:
        return "YES"
    else:
        return "NO"

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)