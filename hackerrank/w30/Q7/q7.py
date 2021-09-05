filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://www.geeksforgeeks.org/%C2%AD%C2%ADkasais-algorithm-for-construction-of-lcp-array-from-suffix-array/
#
import math
import sys

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)


print ins


N=300005
logN = 17

n,q = map(int , ins[0].strip().split())
index=1
ads=""
sizels = [0]*n
sls = [0]*n
als=""
belong=[0]*N
suffix= [0]*N
C = [0]*N
SPLITCHAR =unichr(ord('z')+1)
for i in range(n):
    tp= ins[index+i].strip()
    sizels[i] = len(tp)
    sls[i] = tp
    als = als+ SPLITCHAR 
    ads = ads + tp
    t = len(als)
    als = als +tp
    for j in range(t,len(als)):
        belong[j] = i

for i in range(len(als)):
    suffix[i] = als[i]
m= len(als) -1

for j in range(logN):
    for i in range(m):
        C[i] = ((suffix[i],suffix[min(m+1,i+ 1<<j)]),i)
        C= sorted(C[:m])

   
index = index + n
for i in range(q):
    a,b = map(int , ins[index+i].strip().split())
    print a,b

print unichr(ord('z')+1)
print C[:100]
print als
print suffix[:100]