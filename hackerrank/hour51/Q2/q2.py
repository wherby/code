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


n,m,k = map(int , ins[0].strip().split())
index=1
ls=[0]*n*13
socets =[]
#print ls
def translate(x,y):
	global ls,n,socets
	re =0
	if y == 0 :
		re =x
	elif x ==n:
		re = n + y
	elif y == n:
		re = 2*n +n -x
	elif x ==0:
		re = 4*n -y
	ls[re] =ls[re] +1
	ls[re + 4*n]  =1 +ls[re + 4*n]



for i in range(m):
	x,y= map(int , ins[index+i].strip().split())
	translate(x,y)

for i in range(13*n):
	while ls[i] != 0:
		socets.append(i)
		ls[i] =ls[i] -1
minL = 4*n
x1 = len(socets) - k +1
for i in range(x1):
	tp = socets[i + k -1] - socets[i]
	if tp < minL:
		minL =tp
print minL
