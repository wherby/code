def compsuff(suf1,suf2):
	if suf1[1] == suf2[1]:
		if suf1[2] < suf2[2]:
			return 1
		else:
			return -1
	else:
		if suf1[1] < suf2[1]:
			return 1
		else:
			return -1


class Suffix:
	def __init__(self,strInput):
		self.n = len(strInput)
		self.ls=[]
		for i in range(self.n):
			self.ls.append(strInput[i:])
		self.strInput = strInput
		self.suffixes =[]
		pass

	def getLs(self):
		for i in range(self.n):
			print self.ls[i]


	def buildSuffixArray(self):
		strInput = self.strInput
		n = self.n
		ls =self.ls
		suffixes=[]
		for i in range(n):
			rank0 = ord(strInput[i]) - ord('a')
			rank1 = ord(strInput[i+1]) -ord('a') if i+1 < n else -1 
			suffixes.append([i,rank0,rank1])
		suffixes= sorted(suffixes, cmp = lambda x,y: compsuff(x,y))

		ind=[0] *n

		k = 4
		while k< 2*n:
			rank =0
			prev_rank = suffixes[0][1]
			suffixes[0][1] = rank
			ind[suffixes[0][0]]=0

			for i in range(1,n):
				if suffixes[i][1] == prev_rank and suffixes[i][2] == suffixes[i-1][2]:
					prev_rank = suffixes[1][1]
					suffixes[i][1] = rank
				else:
					prev_rank = suffixes[i][1]
					rank = rank +1
					suffixes[i][1] = rank 

				ind[suffixes[i][0]] = i

			for i in range(n):
				nextindex = suffixes[i][0] + k/2
				suffixes[i][2] = suffixes[ind[nextindex]][1] if nextindex < n else -1

			suffixes= sorted(suffixes, cmp = lambda x,y: compsuff(x,y))



			k= k *2
			pass
		self.suffixes = suffixes


if __name__=="__main__":
	strInput = "banana"
	ax = Suffix(strInput)
	ax.buildSuffixArray()
	ax.getLs()
	#ax.buildSuffixArray()
