def isPrime(n):
	for i in range(2,int(n**0.5)+1):
		if n%i==0:
			return False
	return True



ls = range(2,35000)
ls = filter(isPrime,ls)
print ls