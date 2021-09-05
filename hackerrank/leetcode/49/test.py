def findNumberOfLIS(nums):
	n = len(nums)
	if n == 0 :
		return 0
	mx= []
	for i in range(n):
		tm = [0]*n
		mx.append(tm)
	al =[1]*n
	for i in range(1,n):
		for j in range(n):
			t = n-1-j
			if i+t <n:
				if nums[t] < nums[t+i]:
					al[t] = max(al[t], al[t+i]+1)
	mx = max(al)
	dicls=[0]*mx
	for i in range(n):
		t = al[i] -1
		dicls[t] = dicls[t] +1
	re =1
	print al
	for i in range(mx-1):
		if dicls[i] >0:
			re = re * dicls[i]
	if mx ==1:
		return n
	else:
		return re





nums= [1,2,4,3,5,4,7]
print findNumberOfLIS(nums)