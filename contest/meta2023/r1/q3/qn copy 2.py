#https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d0a5c
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/back_in_black_chapter_2_input.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin
    
    
from collections import defaultdict,deque


def resolve():
    m = int(input())
    ols = input()
    arr =[0]*(m+1)
    for i,a in enumerate(ols,1):
        if a == "1":
            arr[i]=1
    n = int(input())

    cnt = 0
    sm =0
    dic=defaultdict(int)
    for i in range(1,m+1):
        if arr[i] ==1:
            cnt +=1
            dic[i] =1
            for j in range(i,m+1,i):
                arr[j] = 1- arr[j]
    for _ in range(n):
        k = int(input())
        dic[k] +=1
        if dic[k] %2 ==0:
            cnt -=1
        else:
            cnt +=1
        sm += cnt
    return sm

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)