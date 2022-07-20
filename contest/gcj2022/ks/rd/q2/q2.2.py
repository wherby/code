#https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4672b
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

# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]


def roundDp(ls,k):
    n = len(ls)
    pre0=[0]*(n+1)
    pre1 =[0]* (n+1)
    for i in range(n):
        pre0[i+1] = pre0[i]+ ls[i]
        pre1[i+1] = pre1[i] + ls[n-1-i]
    return (pre0,pre1)

def resolve():
    
    n, = tuple(list(map(lambda x: int(x),input().split())))
    ls1  = list(map(lambda x: int(x),input().split()))
    m, =  tuple(list(map(lambda x: int(x),input().split())))
    ls2 = list(map(lambda x: int(x),input().split()))
    k, = tuple(list(map(lambda x: int(x),input().split())))
    pre0,pre1 = roundDp(ls1,k)
    pre2,pre3= roundDp(ls2,k)
    pre =[pre0,pre1,pre2,pre3]
    dp =[[0]*(k+1) for _ in range(n)]
    for i in range(1,k+1):
        dp[0][i] = pre0[i]
    for j in range(1,4):
        for i in range(1,k+1):
            for z in range(i+1):
                dp[j][i]= max(dp[j-1][i],dp[j-])
    
def op(caseidx):
    ret= resolve()
    print("Case #"+str(caseidx+1)+": " + ret)
    

for i in range(int(input())):
    op(i)