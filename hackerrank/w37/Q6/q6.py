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
CONST = 1000000007

def exponenX(base,exponent):
    global CONST 
    if base == 1:
        return 1
    result =1
    while exponent >0:
        if exponent &1:
            result=result *base % CONST
        exponent =exponent >>1
        base =base **2 %CONST
    return result

n,k= map(int , ins[0].strip().split())
if n >3 :
    print 0
else:
    a= exponenX(k,n-1) *(n-1 )% CONST
    print a




