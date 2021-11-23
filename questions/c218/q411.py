import itertools
import collections
class Solution(object):
    def minimumIncompatibility(self, nums, k):
        c = collections.Counter(nums)
        
        for _,v in c.items():
            if v > k:
                return -1
        n = len(nums)
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
        print(validComb)
        visit = [0]*n
        mmn = 10**9
        def dfs(idx,sm,sg):
            #print(idx)
            nonlocal mmn
            if sm >mmn:
                return
            if idx == k:
                mmn = min(mmn,sm)
            for c in validComb:
                #print(c)
                if c[1] & sg !=0: continue
                dfs(idx +1 ,sm + dic[c[0]],sg+c[1])
        dfs(0,0,0)
        return mmn

nums=[7,3,16,15,1,13,1,2,14,5,3,10,6,2,7,15]
nums=[7,3,16,15,1,13,1,2,14,5,3,10,6,2,7,15]
k=8
re = Solution().minimumIncompatibility(nums,k)
print(re)
