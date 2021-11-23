# Timout for combination first...
import itertools
import collections
import functools
class Solution(object):
    def minimumIncompatibility(self, nums, k):
        c = collections.Counter(nums)
        
        for _,v in c.items():
            if v > k:
                return -1
        n = len(nums)
        @functools.lru_cache(None) 
        def getValidComb(ls):
            comb = itertools.combinations(ls,n//k)
            validComb =[]
            for c in comb:
                dic[c] = getCombValue(c)
                if dic[c] != -1:
                    sg =0
                    for i in c:
                        sg += 1<<i
                    validComb.append([c,sg])
            return validComb
        ls =list(range(n))
        comb = itertools.combinations(ls,n//k)
        dic={}
        nums.sort()
        def getCombValue(c):
            tls =[-1]*(n//k)
            idx =0
            re = -1
            for i in c:
                tls[idx] = nums[i]
                idx +=1
            if len(tls) != len(set(tls)):
                re=-1
            else:
                re = tls[-1] -tls[0]
            return re
        validComb =[]
        for c in comb:
            dic[c] = getCombValue(c)
            if dic[c] != -1:
                sg =0
                for i in c:
                    sg += 1<<i
                validComb.append([c,sg])
        #print(validComb)
        visit = [0]*n
        mmn = 10**9
        @functools.lru_cache(None) 
        def dfs(idx,sm,sg):
            nonlocal mmn
            if sm >mmn:
                return
            ls = []
            cnt =0
            for i in range(n):
                if sg& 1<<i ==0:
                    ls.append(i)
            validComb = getValidComb(tuple( ls))
            #print(idx)

            if idx == k:
                mmn = min(mmn,sm)
            for c in validComb:
                #print(c)
                if c[1] & sg !=0: continue
                for i in c[0]:
                    visit[i] =1
                dfs(idx +1 ,sm + dic[c[0]],sg+c[1])
                for i in c[0]:
                    visit[i] =0
        dfs(0,0,0)
        return mmn


re = Solution().minimumIncompatibility([6,3,8,1,3,1,2,2],4)
print(re)