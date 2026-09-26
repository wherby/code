# https://leetcode.cn/contest/weekly-contest-516/problems/longest-subarray-with-at-most-k-distinct-prime-factors/description/

from collections import defaultdict,deque



M = 10**5

pr =list(range(M+1))

for i in range(2,M+1):
    if pr[i] == i:
        for j in range(i,M+1,i):
            pr[j] = i 

def factors(x):
    if x ==0:return [] 
    res = []
    
    while x >1:
        p = pr[x]
        c = 0
        res.append(p)
        while x %p ==0:
            x //= p 
            c +=1
    return res 

class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        ret = 0
        dic =defaultdict(int)
        cnt = 0
        l = 0
        for i,a in enumerate(nums):
            for b in factors(a):
                if dic[b] ==0:
                    cnt +=1
                dic[b]+=1
            
            while cnt >k:
                print(factors(nums[l]),l)
                for b in factors(nums[l]):
                    dic[b] -=1
                    if dic[b] ==0:
                        cnt -=1
                l +=1
            #print(factors(a),a,cnt,dic,l)
            ret =max(ret,i-l+1)
        return ret





re =Solution().longestSubarray(nums = [10,5,7,9,8,3], k = 2)
print(re)
            