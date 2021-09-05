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

istr= ins[0]

vo=['a', 'e', 'i', 'o', 'u', 'y']

v1=map(lambda x : x in vo,istr)

n = len(istr)
isB= True

for i in range(1,n):
	if istr[i] == istr[i-1]:
		isB=False
	if v1[i]== True and v1[i-1] == True:
		isB = False
if isB == True:
	print "Yes"
else:
	print "No"


