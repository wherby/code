#https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d0a5c
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#filename = "input/cheeseburger_corollary_2_validation_input.txt"

filename = "input/line_by_line_input.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin


import math
def resolve():
    N,K = list(map(lambda x: int(x),input().split()))
    k1 = K /100
    t1 = math.log(k1)*(N-1)/N 
    a2 = math.exp(t1)
    return (a2-k1)*100


def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)