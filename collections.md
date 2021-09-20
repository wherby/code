# count number
import collections
count = collections.Counter(nums)

# generate bitmap of prime for a 
primes=[2,3,5,7,11,13,17,19,23,29]
mask = sum(1 <<i  for i,p in enumerate(primes) if a %p ==0)

# find index of value in array:
i = nums.index(1) 


# header
from collections import defaultdict
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left