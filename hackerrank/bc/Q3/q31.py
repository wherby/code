filename = "input/input02.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys
import bisect


if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin

class BigBisect:
	def __init__(self):
		self.Count =80
		self.array=[] 
		for i in range(self.Count):
			self.array.append([])

	def insort_left(self,index,num):
		n = index % self.Count
		bisect.insort_left(self.array[n],num)

	def remove(self,index,num):
		n = index % self.Count
		self.array[n].remove(num)

	def bisectleft(self,num):
		index = 0
		for i in range(self.Count):
			a1 =self.array[i]
			t1 = bisect.bisect_left(a1,num)
			index = index +t1
		return index
	def printS(self):
		print self.array

bs=BigBisect()


ins=[]
for line in inputA:
    ins.append(line)

n,m = map(int , ins[0].strip().split())
al =map(int , ins[1].strip().split())

tnum=0
ttnum =0
dic1 = {}
sl= []
for i in range(m):
	t = al[i]
	if t not in dic1:
		dic1[t] =[1]
	else:
		dic1[t].append(i)
	bs.insort_left(i,t)
	it = bs.bisectleft(t)
	#it =  bisect.bisect_left(sl,t)
	#bisect.insort_left(sl,t)
	#it = sl.index(t)
	tnum = tnum + i -it - len(dic1[t]) +1
ttnum = tnum
#print ttnum
#print ttnum
#print n -m
for i in range(n-m):
	t1 = al[i]
	t = al[i +m]
	it1 = bs.bisectleft(t1)
	tnum = tnum - it1 
	#sl.remove(t1)
	bs.remove(i,t1)
	#print sl
	dic1[t1] =dic1[t1][1:]
	if t not in dic1:
		dic1[t] =[1]
	else:
		dic1[t].append(m+i)
	bs.insort_left(i+m,t)
	#bisect.insort(sl,t)
	#it = sl.index(t)
	it = bs.bisectleft(t)
	tnum = tnum + m -it - len(dic1[t]) 
	#print tnum,sl
	ttnum = ttnum +tnum

print ttnum




