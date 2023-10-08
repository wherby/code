#https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d0a5c
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

from math import sqrt
def get_prime_factor(num):
    # 质因数分解
    res = []
    for i in range(2, int(sqrt(num)) + 1):
        cnt = 0
        while num % i == 0:
            num //= i
            cnt += 1
        if cnt:
            res.append([i, cnt])
        if i > num:
            break
    if num != 1 or not res:
        res.append([num, 1])
    return res

res =[]
def resolve():
    inp = int(input())
    res =[]
    pls = get_prime_factor(inp)
    plss = []
    for a,b in pls:
        plss +=[a]*b
    #print(plss)
    if sum(plss) > 41:
        return -1
    res = plss + [1]*(41- sum(plss))
    if len(res)==0:
        return -1
    else:
        ret =str(len(res)) + " "
    return ret + " ".join([str(a) for a in res])

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)