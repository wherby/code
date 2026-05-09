from typing import List, Tuple, Optional
from collections import defaultdict,deque

def getPrime(n):
    ret = [i for i in range(n+1)]
    for i in range(2,n+1):
        if ret[i] == i:
            for j in range(i*2,n+1,i):
                ret[j] = i
    return ret 
pms = getPrime(10**6+2)

def getFactor(n):
    ret =[]
    cur = n
    while cur !=1:
        b= pms[cur]
        ret.append(b)
        while cur %b ==0:
            cur = cur //b 
    return ret 
    
class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        dic = defaultdict(list)
        for i,a in enumerate(nums):
            dic[a].append(i)
        dp = [n]*n
        cand = deque([(0,n-1)])
        dp[n-1] = 0
        while cand:
            c,idx = cand.popleft()
            if dp[idx]!= c:
                continue 
            dp[idx] = c 
            if idx>0 and dp[idx-1]>c+1:
                dp[idx-1] = c+1
                cand.append((c+1,idx-1))
            if idx<n-1 and dp[idx+1]>c+1:
                dp[idx+1] = c+1
                cand.append((c+1,idx+1))
            for fa in getFactor(nums[idx]):
                for b in dic[fa]:
                    if dp[b] > c+1:
                        dp[b] =c+1
                        cand.append((c+1,b))
                dic[fa]=[]
        return dp[0]

re = Solution().minJumps([5]*10000)
print(re)