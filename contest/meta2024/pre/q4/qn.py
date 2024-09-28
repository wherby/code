#https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d0a5c
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/line_of_delivery_part_1_input.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin


def resolve():
    N,G = list(map(lambda x: int(x),input().split()))
    ls =[]
    for i in range(N):
        inp = int(input())
        ls.append(inp)
    ret = 0
    ls.sort()
    mx = abs(G - ls[0])
    for i ,a in enumerate(ls):
        d =abs(G-a)
        if d <= mx:
            mx = d 
            ret = i 

    return str(N-ret) + " " + str(mx)

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)