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







q,start,end = map(int , ins[0].strip().split())
index=1
vlist=[]
for i in range(q):
	x,y= map(float , ins[index+i].strip().split())
	vlist.append([x,y])
vlist.extend(vlist)

vvlist1=[]
vvlist2=[]
start = min(start,end)
end =max(start,end)
end2 = start + q

p1=vlist[start-1]
for i in range(start,end):
	p2 = vlist[i]
	vvlist1.append([p2[0]-p1[0],p2[1]-p1[1]])
	p1=p2

p1=vlist[end-1]
for i in range(end,end2):
	p2 = vlist[i]
	vvlist2.append([p2[0]-p1[0],p2[1]-p1[1]])
	p1=p2

def getAng(p1,p2):
	x1=p1[0]
	x2=p2[0]
	y1=p1[1]
	y2=p2[1]

	a = (x1 *x2 + y1 * y2) / (math.sqrt(x1**2 + y1**2) *math.sqrt(x2**2 + y2**2))

	a =math.acos(a)
	return a

def getDis(p1):
	x1=p1[0]
	y1=p1[1]
	a= math.sqrt((x1 )**2 + (y1)**2)
	return a

ang1=[0]*len(vvlist1)

for i in range(len(vvlist1)-1):
	tp=[]
	for j in range(i+1,len(vvlist1)):
		vv1=vvlist1[i]
		vv2=vvlist1[j]
		a = getAng(vv1,vv2)
		tp.append(a)
	ang1[i] = tp 


ang2=[0]*len(vvlist2)
for i in range(len(vvlist2)-1):
	tp=[]
	for j in range(i+1,len(vvlist2)):
		vv1=vvlist2[i]
		vv2=vvlist2[j]
		a = getAng(vv1,vv2)
		tp.append(a)
	ang2[i] = tp 
print ang1
ll1=[]
ll2=[]
for i in range(len(vvlist1)):
	p1 = vvlist1[i]
	
	a1 = getDis(p1)
	ll1.append(a1)
for i in range(len(vvlist2)):
	p1 = vvlist2[i]
	a1 = getDis(p1)
	ll2.append(a1)

l1 = sum(ll1)
l2 = sum(ll2)
ml = max(l1,l2)
print ml


