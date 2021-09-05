filename = "input/input04.txt"
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



q, = map(int , ins[0].strip().split())
mtx=[]
for i in range(q):
	mtx.append([0]*q)
for i in range(q):
	for j in range(q):
		mtx[i][j]=[0,0,0]
index =1

def addD(mtx,i,j):
	if i ==0 or j ==0:
		mtx[i][j][0]=1
		mtx[i][j][1]=1
	else:
		mtx[i][j][0]=mtx[i][j-1][0]+1
		mtx[i][j][1]=mtx[i-1][j][1]+1
	mtx[i][j][2]=1
	return mtx[i][j]

for i in range(q):
	t=ins[index+i].strip()
	for j in range(q):
		if t[j]=='*':
			mtx[i][j][0]=0
			mtx[i][j][1]=0
			mtx[i][j][2]=0
		else:
			mtx[i][j]=addD(mtx,i,j)
	pass

def getRange(i,j,r):
	re=[]
	for x in range(-r,r+1):
		my=int(math.sqrt(r**2 - x**2))
		for y in range(-my,my+1):
			if i+y>=0 and i+y<=q-1 and j+x >=0 and j+x <=q-1:
				re.append([i+y,j+x])
	return re 

def computeR(mtx,i,j,r,mxr):
	if r <= mxr:
		return mxr
	rg=getRange(i,j,r)
	isValid=True
	for (x,y) in rg:
		if mtx[x][y][2]==0:
			isValid=False
			break
	if isValid==False:
		return computeR(mtx,i,j,r-1,mxr)
	else:
		return r

mxr=0
for i in range(q):
	for j in range(q):
		if mtx[i][j][2]!=0:
			if mtx[i][j][0] != 1 and mtx[i][j][1] !=1:
				rc=min(mtx[i][j][0]-1,mtx[i][j][1]-1,q-1-i,q-1-j)
				r=computeR(mtx,i,j,rc,mxr)
				if r >mxr:
					mxr=r
print mxr
