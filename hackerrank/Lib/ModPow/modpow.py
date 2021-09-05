CONSTPRIME = 1000000007
def modpow(a,b):
	global CONSTPRIME
	if b ==0:
		return 1
	if b == 1:
		return a
	if b %2 == 1 :
		return a * modpow(a,b-1) % CONSTPRIME
	k = modpow(a, b /2)
	return (k*k)%CONSTPRIME

print modpow(2,1000000000)