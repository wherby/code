
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin

############ ---- Input Functions ---- ############
def inp():
    return (int(input()))
def inlt():
    return (list(map(int,input().split())))
def insr():
    s = input()
    return (list(s[:len(s) - 1]))
def invr():
    return list((map(int,input().split())))

def resolve():
	n,m = tuple(map(int, input().split()))
	if m>=n:
		if n%2==1:
			s = '1 '*(n-1)
			s+=str(m-(n-1))
			ans.append("Yes\n"+s)
		elif n%2==0 and m%2==0:
			s = '1 '*(n-2)
			s+= str((m-(n-2))//2) + ' ' + str((m-(n-2))//2)
			ans.append("Yes\n"+s)
		else:
			ans.append("No")
	else:
		ans.append("No")

    

def op(caseidx):
    resolve()
    
ans =[]
for i in range(int(input())):
    op(i)
for a in ans:
    print(a)