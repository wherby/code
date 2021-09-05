f = open('input/input00.txt')
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

n, = map(int , ins[0].strip().split())