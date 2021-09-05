
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
		return -1
if __name__ == "__main__":
	print BSearch.__doc__
	li = [1,2,3,4,5,6,7,8,9]
	print BSearch(li, 9)