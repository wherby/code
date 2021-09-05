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


#print ins



ls = map(int , ins[1].strip().split())
ls =set(ls)

ls =sorted(ls)
fn =  map(int , ins[3].strip().split())

#!/usr/bin/env python
# BSearch.py
 
def BSearch(li, key):
	"""
	Binary Search:
	Stored the items in a sorted list
	Algorithm: division of integers 
	return the floor of the quotient
	"""
	low = 0
	high = len(li) - 1
	while low <= high:

		mid = (low+high) / 2
		if key == li[mid]:          # found the key
			return mid
		else:
			if key < li[mid]:        # key before the middle
				high = mid -1
			else:                     # key after the middle
				low = mid + 1       
	else:
		return mid



def findN(x):
	global ls
	a1 = BSearch(ls,x)
	n = len(ls)
	#print x,a1
	if x >ls[a1]:
		a1 = n - a1
	elif x < ls[a1]:
		a1= n -a1 +1
	elif x ==ls[a1]:
		a1 = n-a1
	print a1

map(findN,fn)