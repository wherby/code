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


CONSTPRIME = 1000000007
LIM=100001
power=[]
dp=[]
def init():
	global power,dp
	power = [0]*54
	dp=[]
	for i in range(54):
		t = [-1]*LIM
		dp.append(t)
def PowerSum(n,k):
	global CONSTPRIME
	n = n%CONSTPRIME
	if k ==0:
		return n
	if k ==1:
		return n*(n+1)/2 
	if k ==2:
		return n*(n+1)*(2*n+1)/6
	if k==3:
		return n**2 *(n+1)**2 /4
	if k ==4:
		return n *(n+1) *(2*n +1) *(3*n**2 +3*n -1) /30
	if k ==5:
		return  n**2 * (n+1)**2 *(2*n**2+2*n -1) /12
	if k ==6:
		return n*(n+1) *(2*n +1) *(3*n**4 + 6*n**3 - 3*n +1) /42
	if k ==7:
		return n**2*(n+1)**2 *(3*n**4+6*n**3 -n**2-4*n +2) /24
	if k ==8:
		return n *(n+1) *(2*n +1)*(5*n**6 + 15*n**5+5*n**4 -15*n**3 -n**2 +9 *n -3) /90
	if k==9:
		return n**2 * (n+1)**2 *(n**2 + n -1) *(2*n**4 +4*n**3 -n**2 -3*n +3) /20
	if k ==10:
		return n*(n+1)*(2*n +1) *(n**2 +n -1) *(3 * n**6 +9*n**5 +2*n**4 -11*n**3+3*n**2+10*n-5)/66
	print "UNKNOWN expon " + str(k)
	return -1

def count(n,m,k):
	global LIM,ar,power
	if n ==0 :
		#print m,k
		return PowerSum(m,k)
	if m < LIM and dp[n][m] != -1:
		return dp[n][m]
	res = (count(n-1,m,k) - ((count(n-1, m/ar[n], k) * power[n])%CONSTPRIME) +CONSTPRIME) %CONSTPRIME
	if m < LIM :
		dp[n][m]=res
	return res



def solve(m,k):
	global ar,CONSTPRIME,power
	n = len(ar)-1
	for i in range(1,n+1):
		y=ar[i] %CONSTPRIME
		x =1
		for j in range(k):
			x= (x*y)% CONSTPRIME
		power[i]=x
	#print power

	return count(n,m,k)



q, = map(int , ins[0].strip().split())
index=1
for i in range(q):
	init()
	n,expon,ed= map(int , ins[index+i*2].strip().split())
	st =1
	ls= map(int , ins[index+i*2 +1].strip().split())
	ar=[0] +sorted(ls)
	#print expon
	print solve(ed,expon)


