filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys
from decimal import Decimal 

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)




q, = map(int , ins[0].strip().split())
index=1
ls =[]
for i in range(q):
    n,= map(float , ins[index+i].strip().split())
    ls.append(n)
ls = filter(lambda x: x >=90,ls)
x = sum(ls)*1.00 /len(ls) 
a = (x *1000) %10 >=5
x =(int(x*100) + a) *1.0/100  
print("{:.2f}".format(Decimal(x)))