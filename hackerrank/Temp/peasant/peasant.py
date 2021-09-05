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



class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def mulP(self,y):
		x = y.x * self.x - y.y*self.y
		y = y.x*self.y +self.x *y.y
		return Point(x,y)

	def mulPM(self,y,m):
		x = y.x * self.x - y.y*self.y
		y = y.x*self.y +self.x *y.y
		return Point(x%m,y%m)


def exponentiatel(x, n):
	while (n & 1)==0:
		x = x.mulP(x)
		n= n>>1
	p=x
	n=n>>1
	while (n>0):
		x=x.mulP(x)
		if((n & 1) !=0):
			p=p.mulP(x);
		n = n >>1
	return p

def exponentiatelM(x, n,m):
	while (n & 1)==0:
		x = x.mulPM(x,m)
		n= n>>1
	p=x
	n=n>>1
	while (n>0):
		x=x.mulPM(x,m)
		if((n & 1) !=0):
			p=p.mulPM(x,m);
		n = n >>1
	return p


# a= Point(2,0)
# # a= a.mulP(a)
# b =exponentiatel(a,9)
# # print (a.x,a.y)
# print (b.x,b.y)


q, = map(int , ins[0].strip().split())
index=1
for i in range(q):
	a,b,k,m,= map(int , ins[index+i].strip().split())
	pt = Point(a,b)
	re = exponentiatelM(pt,k,m)
	print str(re.x) + " " + str(re.y)

	