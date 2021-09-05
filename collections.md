# count number
import collections
count = collections.Counter(nums)

# generate bitmap of prime for a 
primes=[2,3,5,7,11,13,17,19,23,29]
mask = sum(1 <<i  for i,p in enumerate(primes) if a %p ==0)