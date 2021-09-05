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




# A Dynamic Programming based Python program for LPS problem
# Returns the length of the longest palindromic subsequence in seq
def lps(str):
    n = len(str)
 
    # Create a table to store results of subproblems
    L = [[0 for x in range(n)] for x in range(n)]
 
    # Strings of length 1 are palindrome of length 1
    for i in range(n):
        L[i][i] = 1
 
    # Build the table. Note that the lower diagonal values of table are
    # useless and not filled in the process. The values are filled in a
    # manner similar to Matrix Chain Multiplication DP solution (See
    # http://www.geeksforgeeks.org/dynamic-programming-set-8-matrix-chain-multiplication/
    # cl is length of substring
    for cl in range(2, n+1):
        for i in range(n-cl+1):
            j = i+cl-1
            if str[i] == str[j] and cl == 2:
                L[i][j] = 2
            elif str[i] == str[j]:
                L[i][j] = L[i+1][j-1] + 2
            else:
                L[i][j] = max(L[i][j-1], L[i+1][j]);
 
    return L[0][n-1]


# A Dynamic Programming based Python program for LPS problem
# Returns the length of the longest palindromic subsequence in seq
def lpsList(lsstr):
    n = len(lsstr)
 
    # Create a table to store results of subproblems
    L = [[0 for x in range(n)] for x in range(n)]
 
    # Strings of length 1 are palindrome of length 1
    for i in range(n):
        L[i][i] = 1
 
    # Build the table. Note that the lower diagonal values of table are
    # useless and not filled in the process. The values are filled in a
    # manner similar to Matrix Chain Multiplication DP solution (See
    # http://www.geeksforgeeks.org/dynamic-programming-set-8-matrix-chain-multiplication/
    # cl is length of substring
    for cl in range(2, n+1):
        for i in range(n-cl+1):
            j = i+cl-1
            if lsstr[i] == lsstr[j] and cl == 2:
                L[i][j] = 2
            elif lsstr[i] == lsstr[j]:
                L[i][j] = L[i+1][j-1] + 2
            else:
                L[i][j] = max(L[i][j-1], L[i+1][j]);
 
    return L[0][n-1]



n,q,m = map(int , ins[0].strip().split())
index=1
replacels=[]
for i in range(q):
	x,y= map(int , ins[index+i].strip().split())
	replacels.append([x,y])
lsorg = map(int , ins[q+1].strip().split())

dic1={}
rg=[]
for i in range(q):
	x,y = replacels[i]
	if (x not in dic1) and (y not in dic1):
		dic1[x] =1
		dic1[y] =1
		rg.append({x:1,y:1})
	elif (x not in dic1) and (y in dic1):
		dic1[x] =1
		m = len(rg)
		for j in range(m):
			if y in rg[j]:
				rg[j][x] =1
	elif (x in dic1) and (y not in dic1):
		dic1[y] =1
		m = len(rg)
		for j in range(m):
			if x in rg[j]:
				rg[j][y]=1
	elif (x in dic1) and (y in dic1):
		xj=0
		yj=0
		m = len(rg)
		for j in range(m):
			if x in rg[j]:
				xj = j
			if y in rg[j]:
				yj =j
		if xj != yj:
			for p in rg[yj].keys():
				rg[xj][p]=1
			#rg[xj].extend(rg[yj])
			rg.remove(rg[yj])
#print rg
dic2 = {}
m = len(rg)
for i in range(m):
	tp = rg[i]
	minx = min(tp)
	for j in tp:
		dic2[j] =minx

def transls(lsorg, dic2):
	m =len(lsorg)
	for i  in range(m):
		t = lsorg[i]
		if t in dic2:
			lsorg[i] = dic2[t]
	return lsorg
lstrans= transls(lsorg,dic2)
print lpsList(lstrans)
