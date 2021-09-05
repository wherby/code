#https://www.hackerrank.com/contests/w23/challenges/enclosure
filename = "input/input03.txt"
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

halfSize=0
def checkR(R):
	global ls,full,mx
	smR=0.0
	for i in ls:
		if halfSize ==1 and i == mx:
			smR=smR + math.pi -math.asin(i/2/R)
		else:
			smR=smR + math.asin(i/2/R)
	if smR < math.pi:
		return 1
	else:
		return 0





q, = map(int , ins[0].strip().split())
ls = map(float , ins[1].strip().split())
mx = max(ls)
#print ls
#print mx
if(checkR(mx/2)):
	halfSize=1
#print "halfSize " +str(halfSize) 
left = mx/2
right= 100000000
deta = 1e-9
#print left
while right - left >deta:
	mid = (right + left) /2
	if(checkR(mid)^halfSize):
		right=mid
	else:
		left=mid
#print "rr"
#print right, mid

R=right
#print ls
res=[[0.0,0.0]]
#print res
if halfSize == 1 and mx == ls[0]:
	porg=[-math.sqrt(R**2 - (ls[0]/2)**2),ls[0]/2]
	argSum= -math.asin(ls[0]/2/R)
else:
	porg=[math.sqrt(R**2 - (ls[0]/2)**2),ls[0]/2]
	argSum=math.pi + math.asin(ls[0]/2/R)
#print porg
#print porg

itialV=[0,-R]

#print itialV
#print "xxxx"
#print R *math.sin(argSum)

for i in range(q-1):
	t1=ls[i]
	if halfSize == 1 and t1 == mx:
		argi= math.pi-math.asin(t1/2/R)
	else:
		argi= math.asin(t1/2/R)
	argSum =argSum - 2*argi
	x= R *math.cos(argSum) + porg[0]
	y= R *math.sin(argSum) + porg[1]
	res.append([x,y])

for i in res:
	print i[0]
	print i[1]
	print 