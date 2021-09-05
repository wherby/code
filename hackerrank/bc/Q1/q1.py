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


a=ins[0].strip()
def validEmail(a):
	if len(a) == 18:
		b = a[5:]
		c =a[:5]
		if b =="@hogwarts.com":
			isB=True
			for i in range(5):
				t = c[i]
				if t <= 'z' and t>='a':
					pass
				else:
					isB =False
			return isB
		else:
			return False 
	else:
		return False

re= validEmail(a)
if re ==True:
	print "Yes"
else:
	print "No"