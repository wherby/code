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

def visit(fr,vi,dest):
    if fr <=vi and vi <=dest:
        return dest-fr
    elif fr <= dest and dest <=vi:
        return vi *2 - fr-dest
    elif vi <=fr and fr <= dest:
        return fr -vi + dest -vi
    elif dest <= fr and fr <=vi:
        return vi- fr + vi -dest
    elif vi <= dest and dest <=fr:
        return fr -vi + dest -vi 
    else:
        return fr - dest 

def resolve():
    ls = input().split(" ")
    ls = [int(x) for x in ls]
    N,P = ls[0],ls[1]
    lls = []
    for _ in range(N):
        ls = input().split(" ")
        ls = [int(x) for x in ls]
        lls.append(ls)
    kls = [[min(ls),max(ls)] for ls in lls]
    dp =[[10 **25]*2 for _ in range(N)]
    dp[0][1] = kls[0][1]
    dp[0][0] = kls[0][1]*2 -kls[0][0]
    for i in range(1,N):
        dp[i][0] = min(dp[i-1][0]+ visit(kls[i-1][0],kls[i][1],kls[i][0]),dp[i-1][1]+ visit(kls[i-1][1],kls[i][1],kls[i][0]))
        dp[i][1] = min(dp[i-1][0]+ visit(kls[i-1][0],kls[i][0],kls[i][1]),dp[i-1][1]+ visit(kls[i-1][1],kls[i][0],kls[i][1]))
    #print(dp)
    return min(dp[N-1][0],dp[N-1][1])
    
def op(caseidx):
    ret= resolve()
    print("Case #"+str(caseidx+1)+": " + str(ret))
    

for i in range(int(input())):
    op(i)