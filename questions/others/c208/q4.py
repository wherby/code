import itertools
class Solution(object):
    def maximumRequests(self, n, requests):
        m = len(requests)
        cand = [i for i in range(m)]
        def verify(kcls):
            for kc in kcls:
                ls =[0]*n
                for i in kc:
                    f,t = requests[i]
                    ls[f] -=1
                    ls[t] +=1
                if all(map(lambda x:x ==0,ls)):
                    return True
            return False
        for k in range(m,-1,-1): 
            kcls = itertools.combinations(cand,k)
            if verify(kcls):
                return k
re = Solution().maximumRequests(n = 5, requests = [[0,3],[1,0],[0,1],[1,2],[2,0],[3,4]])
print(re)
            
