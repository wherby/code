filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
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


class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return 'Node ['+str(self.value)+']'

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def insert(self, x):
        if self.first == None:
            self.first = Node(x, None)
            self.last = self.first
        elif self.last == self.first:
            self.last = Node(x, None)
            self.first.next = self.last
        else:
            current = Node(x, None)
            self.last.next = current
            self.last = current

    def addList(self,listAnother):
        self.last.next = listAnother.first
        self.last = listAnother.last

    def __str__(self):
        if self.first != None:
            current = self.first
            out = 'LinkedList [\n' +str(current.value) +'\n'
            while current.next != None:
                current = current.next
                out += str(current.value) + '\n'
            return out + ']'
        return 'LinkedList []'

    def clear(self):
        self.__init__()

def partitian(ls,grap):
	global grapPart
	ct =0
	n = len(ls)
	for s1,e1 in grap:
		if ls[s1] ==0 and ls[e1]==0:
			ct = ct+1
		if ls[s1] !=0 and ls [e1]!= 0:
			a1= ls[s1]
			b1= ls[e1]
			if a1 != b1:
				for i in range(n):
					if ls [i] == b1:
						ls[i] = a1
		if ls[s1] ==0:
			ls[s1] = ct
		if ls [e1] == 0:
			ls[e1] = ct
	for i in range(1,ct+1):
		grapPart.append({})
	for i in range(1,n):
		t = ls[i]-1
		grapPart[t][i] =1


def getStartPoint(grap):
	lls=[0]*(n+1)
	for s1,e1 in grap:
		lls[e1] = 1
	re =[]
	lls=lls[1:]
	index = 1
	for i in lls:
		if i ==0:
			re.append(index)
		index =index +1
	return re

def generateLinListTree(grap):
	global llst
	for s1,e1 in grap:
		llst[s1].last.next = llst[e1].first

n,m,q = map(int , ins[0].strip().split())
ls= [0]*(n+1)
dic1={}
grapPart=[]
dic2={}
index=1
grap=[]
adjL=[]
for i in range(n+1):
	adjL.append([])
for i in range(m):
	s1,e1= map(int , ins[index+i].strip().split())
	grap.append((s1,e1))
	adjL[s1].append(e1)
grap=sorted(grap,key = lambda x: x[0])

partitian(ls,grap)

getStartPoint(grap)

llst=[]
for i in range(n+1):
	t = LinkedList()
	t.insert(i)
	llst.append(t)
generateLinListTree(grap)

for i in range(n+1):
	print llst[i]

print grapPart
print ls