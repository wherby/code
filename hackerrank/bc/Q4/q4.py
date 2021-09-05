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




			 

m,n, = map(int , ins[0].strip().split())
matrix = []
for i in range(m):
	tp = map(int , ins[i+1].strip().split())
	matrix.extend(tp)

mn =m*n
vmatrix =[1]*mn
bmatric =[1]*mn
vvmaxtrix = [0]*mn
bvmatrix =[1]*mn
fsmatrix = [0]*mn


for i in range(m):
	for j in range(n-1):
		if matrix[i*n + j+1] < matrix[i*n + j]:
			bmatric[i *n +j] =0
for j in range(n):
	for i in range(m-1):
		if matrix[(i+1)*n + j] < matrix[i*n +j]:
			bvmatrix[i*n +j]=0

xzlist=[]
for i in range(m):
	tp =[]
	for j in range(n):
		if bmatric[i*n +j] == 0:
			tp.append(j)
	xzlist.append(tp)
for i in range(m):
	index =0
	for j in range(n):
		if bmatric[i*n + n-1-j] ==0:
			index =j
			vmatrix[i*n + n-1-j] =1

		else:
			vmatrix[i*n + n-1-j] = j+1 -index

for j in range(n):
	index =0
	for i in range(m):
		if bvmatrix[(m-1-i)*n +j] == 0:
			index =i
			vvmaxtrix[(m-1-i)*n+ j] =0
		else:
			vvmaxtrix[(m-1-i)*n +j]=i-index
	



#print vmatrix
tsum = 0
for i in range(m):
	for j in range(n):
		tsum = vmatrix[i*n +j] + tsum
		tsum = vvmaxtrix[i*n +j] + tsum

#print tsum

def searchSqur(t,i,j):
	global m,n,matrix,vmatrix,fsmatrix
	possibalSqur=[]
	num =0
	index =fsmatrix[i*n +j]

	for t1 in range(t,1,-1):
		while(i+index+1 <m and vmatrix[(i+index +1)*n + j] >= t1):
			if   matrix[(i+index) *n + j + t1-1 ] <= matrix[(i+index +1)*n +j]:
				index = index +1
			else:
				if t1 == t :
					fsmatrix[i *n +j+1] = index
					if index !=0 and i+1<m and t == vmatrix[(i+1)*n +j] :
						fsmatrix[(i+1)*n +j] = index-1
				break
		#print index,t1
		num = num + index

	return num

squrls=[]

for i in range(m):
	for j in range(n):
		if vmatrix[i*n +j] >=2:
			t = vmatrix[i* n +j]
			re = searchSqur(t,i,j)
			tsum = tsum +re


#print vmatrix

#print vvmaxtrix

print tsum
#print vmatrix