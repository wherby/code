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



def Simplify(a, b):
    # Divide a and b by their gcd
    c, d= a, b 
    while d != 0:
        c, d= d, c % d
    return (a / c, b / c)

def SAXPY(A, X, Y):
    # Compute A.X + Y, where A, X and Y are fractions
    S= Simplify(A[0] * X[0], A[1] * X[1])
    S= Simplify(S[0] * Y[1] + S[1] * Y[0], S[1] * Y[1])
    return S

def GetKthFaulhaber(K):
    Pascal= [[1]]
    for i in range(1, K + 2):
        Pascal.append([1])
        for j in range(1, i):
            Pascal[i].append(Pascal[i-1][j-1] + Pascal[i-1][j])
        Pascal[i].append(1)

    # Compute the Faulhaber polynomial
    for k in range(K + 1):
        # Initialize the leading coefficient
        S= [(1, k+1)]

        # Compute the next coefficients from the triangular system
        for i in range(k):
            T= (0, 1)
            for j in range(i + 1):
                # Accumulate, with alternating signs
                T= SAXPY(S[j], Simplify(Pascal[k + 1 - j][k - 1 - i], (i - k if (i + j) & 1 else k - i)), T)
            S.append(T)
    return S

def exponen(base,exponent):
	CONST = 1000000009
	if base == 1:
		return 1
	result =1
	while exponent >0:
		if exponent &1:
			result=result *base % CONST
		exponent =exponent >>1
		base =base **2 %CONST
	return result

def GenExpoMofN(n,m):
	re =[0]*m
	CONST = 1000000009
	tp = 1
	for i in range(m):
		tp = tp * n
		tp = tp %CONST
		re[i] = tp
	return re


def ComputeFaulbaberN(n,fls):
	CONST = 1000000009
	m = len(fls)
	total = 0
	expls = GenExpoMofN(n,m)
	for i in range(m,0,-1):
		a,b = fls[m-i]
		a= float(a)
		tp = expls[i-1]* a/ b
		total = tp + total
	total = total -1
	total = int(total) %CONST
	print total


q, = map(int , ins[0].strip().split())
index=1
dic1 ={}
dic2={}
for i in range(1):
	dic2={}
	n,k= map(int , ins[index+i].strip().split())
	if k not in dic1:
		Fls = GetKthFaulhaber(k)
		dic1[k] = Fls
	else:
		Fls = dic1[k]
	ComputeFaulbaberN(n-1,Fls)
