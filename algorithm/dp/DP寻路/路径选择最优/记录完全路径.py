# https://leetcode.cn/problems/prime-subset-selection-ii/
def get_prime(n):
    visited=[0]*(n+2)
    res =[]
    for i in range(2,n+1):
        if visited[i]: continue
        res.append(i)
        for j in range(i,n+1,i):
            visited[j] =1
    return set(res)

class Solution:
    def maxPrimeSubset(self, n: int, s: int) -> list[int]:
        dp = [None]*(s+1)
        dp[0] =(0,[])
        primes = sorted(get_prime(n))
        for p in primes:
            for w in range(s,p-1,-1):
                if dp[w-p] is not None:
                    ncnt = dp[w-p][0]+1
                    npath = dp[w-p][1] + [p]
                    if dp[w] is None:
                        dp[w] = (ncnt,npath)
                    else:
                        ccnt,cpath = dp[w]
                        if ncnt < ccnt:
                            dp[w] = (ncnt,npath)
                        elif ncnt==ccnt and npath < cpath:
                            dp[w] = (ncnt,npath)
        for a in range(s,0,-1):
            if dp[a] is not None:
                return dp[a][1]
        return []
