filename = "input/input01.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://www.hackerrank.com/contests/w24/challenges/simplified-chess-engine

import math
import sys
import copy

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)

ChessMapBits=[0]*16
ChessMapForA=[0]*16
ChessMapForB=[0]*16
dic1={"A1":0,"A2":1,"A3":2,"A4":3,
	   "B1":4,"B2":5,"B3":6,"B4":7,
	   "C1":8,"C2":9,"C3":10,"C4":11,
	   "D1":12,"D2":13,"D3":14,"D4":15}


xlist=['A','B','C','D']
ylist=['1','2','3','4']
dicx={'A':0,'B':1,'C':2,'D':3}
dicy={'1':0,'2':1,'3':2,'4':3}

CHESSMAPLIST=[]

isAWIN=False
isBWIN=False


def getNextMove(point,movFun,AorB):
	global ChessMapBits,ChessMapForA,ChessMapForB,dic1
	mvList=[]
	point1=movFun(point)
	while point1 !=point:
		t1 = dic1[point1]
		if ChessMapBits[t1] == AorB:
			break
		elif ChessMapBits[t1] != 0:
			mvList.append(point1)
			break
		else:
			mvList.append(point1)
			point = point1
			point1 =movFun(point)
	return mvList

def movMov(chess,point,AorB=1):
	mvs=[]
	if chess == 'Q':
		mvs= moveQueen(point,AorB)
	if chess == 'N':
		mvs= movKight(point,AorB)
	if chess == 'R':
		mvs= moveRock(point,AorB)
	if chess == 'B':
		mvs = moveBishop(point,AorB)
	return mvs


def movKight(point,AorB =1):
	global xlist,ylist,dicx,dicy,ChessMapBits,dic1
	x=point[0]
	y=point[1]
	x1 = dicx[x]
	y1 = dicy[y]
	movList= [(x1+1,y1+2),(x1+1,y1-2),(x1+2,y1+1),(x1+2,y1-1),(x1-1,y1+2),(x1-1,y1-2),(x1-2,y1+1),(x1-2,y1-1)]
	movList =filter(lambda x: x[0]>=0 and x[0]<=3 and x[1]>=0 and x[1]<=3,movList)
	movListStr=map(lambda x: xlist[x[0]] + ylist[x[1]],movList)
	movListStr = filter(lambda x: ChessMapBits[dic1[x]] != AorB ,movListStr)
	return movListStr

def moveQueen(point,AorB = 1):
	global QUEENMOVE
	mvListLS = map(lambda x: getNextMove(point,x, AorB),QUEENMOVE)
	mvList=[]
	for lis in mvListLS:
		mvList.extend(lis)
	return mvList

def moveBishop(point,AorB = 1):
	global BISHOPMOVE
	mvListLS = map(lambda x: getNextMove(point,x, AorB),BISHOPMOVE)
	mvList=[]
	for lis in mvListLS:
		mvList.extend(lis)
	return mvList

def moveRock(point,AorB = 1):
	global ROOKMOVE
	mvListLS = map(lambda x: getNextMove(point,x, AorB),ROOKMOVE)
	mvList=[]
	for lis in mvListLS:
		mvList.extend(lis)
	return mvList




def updateChess(chessListA,chessListB):
	global ChessMapBits,ChessMapForA,ChessMapForB,dic1
	ChessMapBits=[0]*16
	ChessMapForA=[0]*16
	ChessMapForB=[0]*16

	for c1 in chessListA:
		t1=c1[1]+c1[2]
		i1=dic1[t1]
		ChessMapBits=1

	for c1 in chessListB:
		t1=c1[1]+c1[2]
		i1=dic1[t1]
		ChessMapBits=2

	for c1 in chessListA:
		point=c1[1]+c1[2]
		

def updateChessDirty(chessListA,chessListB):
	global ChessMapBits,ChessMapForA,ChessMapForB,dic1
	ChessMapBits=[0]*16
	ChessMapForA=[0]*16
	ChessMapForB=[0]*16

	for c1 in chessListA:
		t1=c1[1]+c1[2]
		i1=dic1[t1]
		ChessMapBits[i1]=1

	for c1 in chessListB:
		t1=c1[1]+c1[2]
		i1=dic1[t1]
		ChessMapBits[i1]=2

	for c1 in chessListA:
		point=c1[1]+c1[2]
		res= movMov(c1[0],point)
		for re1 in res:
			i1 =dic1[re1]
			ChessMapForA[i1] =1

	for c1 in chessListB:
		point=c1[1]+c1[2]
		res= movMov(c1[0],point)
		for re1 in res:
			i1 =dic1[re1]
			ChessMapForB[i1] =1





def moveRight(point):
	global xlist,ylist,dicx,dicy
	x=point[0]
	y=point[1]
	if x != 'D':
		x1=dicx[x]+1
		p1 = xlist[x1] +y
		return p1
	else:
		return point

def moveLeft(point):
	global xlist,ylist,dicx,dicy
	x=point[0]
	y=point[1]
	if x != 'A':
		x1=dicx[x]-1
		p1 = xlist[x1] +y
		return p1
	else:
		return point

def moveUp(point):
	global xlist,ylist,dicx,dicy
	x=point[0]
	y=point[1]
	if y != '4':
		y1=dicy[y] +1
		p1 = x +ylist[y1]
		return p1
	else:
		return point

def moveDown(point):
	global xlist,ylist,dicx,dicy
	x=point[0]
	y=point[1]
	if y != '1':
		y1=dicy[y] -1
		p1 = x +ylist[y1]
		return p1
	else:
		return point

def moveRightUp(point):
	global xlist,ylist,dicx,dicy
	x=point[0]
	y=point[1]
	if x != 'D' and y != '4':
		x1=dicx[x]+1
		y1=dicy[y]+1
		p1 = xlist[x1] +ylist[y1]
		return p1
	else:
		return point

def moveLeftDown(point):
	global xlist,ylist,dicx,dicy
	x=point[0]
	y=point[1]
	if x != 'A' and y != '1':
		x1=dicx[x]-1
		y1=dicy[y]-1
		p1 = xlist[x1] +ylist[y1]
		return p1
	else:
		return point

def moveLeftUp(point):
	global xlist,ylist,dicx,dicy
	x=point[0]
	y=point[1]
	if y != '4' and x !='A':
		x1=dicx[x] -1
		y1=dicy[y] +1
		p1 = xlist[x1] +ylist[y1]
		return p1
	else:
		return point

def moveRightDown(point):
	global xlist,ylist,dicx,dicy
	x=point[0]
	y=point[1]
	if y != '1' and x != 'D':
		x1=dicx[x] +1
		y1=dicy[y] -1
		p1 = xlist[x1] +ylist[y1]
		return p1
	else:
		return point

def isQueenAttacked(chessListA,chessListB,AorB):
	global ChessMapBits,ChessMapForA,ChessMapForB,dic1
	updateChessDirty(chessListA,chessListB)
	QB=0
	if AorB == 1:
		chessList=chessListB
		chessMap = ChessMapForA
	else:
		chessList=chessListA
		chessMap = ChessMapForB
	# print chessListA,chessListB
	#print chessMap
	for x in chessList:
		if x[0] == 'Q':
			p1=x[1]+x[2]
			QB = dic1[p1]

	if chessMap[QB] ==1 :
		return True
	else:

		return False

def moveOneChess(chessListA,chessListB,AorB):
	global ChessMapBits,ChessMapForA,ChessMapForB,dic1, isAWIN,isBWIN
	if isQueenAttacked(chessListA,chessListB,AorB):
		return []
	mapListList=[]
	if AorB ==1:
		chessList = chessListA
		chessListOther = chessListB
		BorA=2
	else:
		chessList = chessListB
		chessListOther =chessListA
		BorA=1
	for i in range(len(chessList)):
		updateChessDirty(chessListA,chessListB)
		chess = chessList[i]
		t1=chess[0]
		t2=chess[1] + chess[2]
		movList = movMov(t1,t2,AorB)
		
		mapList = map(lambda x:updateChessMap(chessListA,chessListB,t2,x),movList)
		
		mapList = filter(lambda x: not isQueenAttacked(x[0],x[1],AorB),mapList) 
		print mapList

		mapListList.extend(mapList)
	return mapListList



def updateChessMap(chessListA,chessListB,fr,tD):
	cpA = copy.deepcopy(chessListA)
	cpB =copy.deepcopy(chessListB)
	for che in cpA:
		t1 = che[0]
		t2 = che[1] + che[2]
		if t2 == fr:
			che[1] = tD[0]
			che[2] = tD[1]
	for che in cpB:
		t1 = che[0]
		t2 = che[1] + che[2]
		if t2 == tD:
			cpB.remove(che)
	return (cpA,cpB)






def getValueCHESS(chessList):
	va=0
	for x in chessList:
		if x[0] == 'Q':
			va =va +20
		elif x[0] =='B':
			va =va +10
		else:
			va =va +5
	return va

def getBQueenMove(chessListB):
	global ChessMapBits,ChessMapForA,ChessMapForB,dic1
	for x in chessListB:
		if x[0] == 'Q':
			p1=x[1]+x[2]
	mvList = movMov('Q',p1,2)
	mvList = filter(lambda x : ChessMapForA[dic1[x]] != 1,mvList)
	return len(mvList)


def solveChessDirty(chessListA,chessListB,movNum):
	global ChessMapBits,ChessMapForA,ChessMapForB,dic1
	updateChessDirty(chessListA,chessListB)

	if movNum ==1:
		if isQueenAttacked(chessListA,chessListB,1) ==1:
			print "YES"
		else:
			print "NO"
	else:
		va =getValueCHESS(chessListA)
		a =getBQueenMove(chessListB)
		if a <=1 and va > 20:
			print "YES"
			return
		if va >=30:
			print "YES"
		else:
			print "NO"

def solveChessDirty2(CHESSMAPLIST,movNum):
	global ChessMapBits,ChessMapForA,ChessMapForB,dic1
	AorB =1
	while movNum !=0:

		chessMap = map(lambda x: moveOneChess(x[0],x[1],AorB),CHESSMAPLIST)
		t =[]
		for x in chessMap:
			t.extend(x)
		#print t
		CHESSMAPLIST =t
		if AorB ==1:
			AorB =2
		else:
			AorB =1
		movNum = movNum -1
	if len(CHESSMAPLIST) ==0:
		print "YES"
	else:
		print "NO"
	
	


QUEENMOVE=[moveRight,moveLeft,moveUp,moveDown,moveRightUp,moveLeftDown,moveRightDown,moveLeftUp]
BISHOPMOVE =[moveRight,moveLeft,moveUp,moveDown]
ROOKMOVE =[moveLeftUp,moveLeftDown,moveRightDown,moveRightUp]

q, = map(int , ins[0].strip().split())
index=1
for i in range(q):
	isAWIN=False
	isBWIN=False
	a,b,c= map(int , ins[index].strip().split())
	n1 = a + b 
	chessListA=[]
	chessListB=[]
	CHESSMAPLIST=[(chessListA,chessListB)]
	for j in range(a):
		chessT = ins[index+ 1 + j].strip().split()
		chessListA.append(chessT)
	for j in range(b):
		chessT = ins[index+ 1 +a + j].strip().split()
		chessListB.append(chessT)
	index = index +1 + n1
	solveChessDirty(chessListA,chessListB,c)









