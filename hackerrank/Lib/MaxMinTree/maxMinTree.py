class MaxTree:
	def __init__(self,ls,n=128):
		n2 = n*2
		self.n = n
		self.ls = [0] * n2
		nls = len(ls)
		for i in range(nls):
			self.ls[i] = ls[i]
			self.ls[i+n] = ls[i]
		m = 2
		idx=n
		idx2=n
		while m<= n:
			k = n/m
			for i in range(k):
				self.ls[idx + i] = max(self.ls[idx2 + i *2], self.ls[idx2 + i *2 +1])
			m = m*2
			if m ==2:
				idx2 = n
			else:
				idx2 = idx
			idx = idx +k

	def getBase2(self,x):
		try:
			#print "Pre ",x
			re =int(x,2)

		except:
			re =0
		return re

	def getMax(self,prefix,remain):
		rl = len(remain)
		base = 0
		pn= rl
		if rl == 0:
			idx = self.getBase2(prefix)
		else:
			for i in range(1,pn):
				base = base + 2 **(self.nn - i )
				##print i,2 **(self.nn - i -1)
			p1 = self.getBase2(prefix)
			idx = base + p1
			idx = idx + self.n
		#print idx
		#print self.ls[idx]
		return self.ls[idx]

	def getBin(self,x):
		return lambda x: format(x, 'b').zfill(self.nn)

	def getLeftAndRight(self,startB,endB):
		get_bin = lambda x, n: format(x, 'b').zfill(n)
		k = 0
		NN = self.nn
		while k < self.nn -1:
			if startB[k] == endB[k]:
				k = k+1
			else:
				break
		maxArray=[]

		for i in range(k,NN):
			t = startB[i]
			if t == '0':
				a1 = startB[:i+1]
				nextB = int(a1,2) +1
				nextB =get_bin(nextB,i)
				x1 = self.getMax(nextB,startB[i+1:])
				maxArray.append(x1)
			if i == NN-1:
				x1 = self.getMax(startB[i+1:],startB[i+1:])
				maxArray.append(x1)
			v = endB[i]
			if v == '1':
				a1 = endB[:i+1]
				preB = int(a1,2) -1
				preB =get_bin(preB,i)
				x1 = self.getMax(preB,endB[i+1:])
				#print preB," ",endB[i+1:]," ",x1
				maxArray.append(x1)
			if i == NN-1:
				x1 = self.getMax(endB[i+1:],endB[i+1:])
				maxArray.append(x1)
		return maxArray


	def find(self,start,end):
		nB="{0:b}".format(self.n)
		get_bin = lambda x, n: format(x, 'b').zfill(n)
		nbN = len(nB)-1
		self.nn = nbN
		startB=str(get_bin(start,nbN))
		endB=str(get_bin(end,nbN))
		maxArray =self.getLeftAndRight(startB,endB)
		return max(maxArray)






if __name__=="__main__":
	a= range(40)
	b = MaxTree(a,64)
	b.find(1,40)
	for i in range(40):
		for j in range(i+1,41):
			x1 = b.find(i,j)
			if x1 == j-1:
				print x1, i,j
	pass