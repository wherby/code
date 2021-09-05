filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)


def findNext(gp,index,priviousEnd):
    n = len(gp)
    for i in range(index+1, n):
        t = gp[i]
        if t[0] >= priviousEnd:
            return (t[1],i)
    return (100000000000,1000)



def getResult(names,starts,ends):
    n =len(names)
    re = [-1] *n
    gp1 =[]
    gp2 =[]
    for i in range(n):
        if names[i] in ["E","C"]:
            gp1.append([starts[i],ends[i]])
        else:
            gp2.append([starts[i],ends[i]])
    gp1=sorted(gp1,key=lambda x: x[1])
    gp2=sorted(gp2,key=lambda x: x[1])
    dp1 = [float("inf")] *(n+1)
    dp2 = [float("inf")]*(n+1)
    dp =[float("inf")]*(n+1)
    dp1[0]=dp2[0] =dp[0]=[0,-1,-1]
    for i in range(1,n+1):
        dp11Index = dp1[i-1][1] +1
        dp11= float("inf")
        if dp11Index<len(gp1):
            dp11=gp1[dp11Index][1]
        dp22Index = dp2[i-1][2] +1
        dp22 = float("inf")
        if dp22Index < len(gp2):
            dp22 = gp2[dp22Index][1]
        dp21End = dp2[i-1][0]
        dp21Index = dp2[i-1][1]
        dp21,indexDp21 =findNext(gp1,dp21Index,dp21End)
        dp12End =dp1[i-1][0]
        dp12Index = dp1[i-1][2]
        dp12,indexDp12 = findNext(gp2,dp12Index,dp12End)
        if dp11 <= dp21:
            dp1[i] = [dp11,dp1[i-1][1]+1,dp1[i-1][2]]
        else:
            dp1[i] = [dp21,indexDp21,dp2[i-1][2]]
        if dp22 <=dp12:
            dp2[i] = [dp22,dp2[i-1][1],dp2[i-1][2]+1]
        else:
            dp2[i] = [dp12,dp1[i-1][1],indexDp12]
    re =[]
    #print dp1,dp2
    for i in range(1,n+1):
        tp = min(dp1[i][0],dp2[i][0])
        if tp <10000000000:
            re.append(tp)
        else:
            re.append(-1)
    re =map(str,re)
    re = " ".join(re)
    print re



NUM, = map(int , ins[0].strip().split())
index = 1
for i in range(NUM):
    m,n =  map(int , ins[index + i*4].strip().split())
    NAME =  ins[index +1 + i*4].strip().split()
    starts =  map(int , ins[index+2 + i*4].strip().split())
    ends = map(int , ins[index +3+ i*4].strip().split())
    getResult(NAME,starts,ends)
