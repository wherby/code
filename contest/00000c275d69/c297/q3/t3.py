import itertools
class Solution(object):
    def distributeCookies(self, cookies, k):
        """
        :type cookies: List[int]
        :type k: int
        :rtype: int
        """
        l,r = max(cookies),sum(cookies)
        n = len(cookies)
        ls = list(itertools.permutations(cookies))
        def verify(mid,ls):
            cnt =0
            acc =0
            for a in ls:
                if a + acc <=mid:
                    acc +=a
                else:
                    cnt +=1
                    acc =a 
            if acc !=0:
                cnt +=1
            #print(ls,mid,cnt)
            return cnt <=k
        def verifyAll(mid): 
            #print("aaa",ls)
            for tls in ls:
                if verify(mid,tls):
                    return True
            return False 
        while l<r:
            mid = (l+r)>>1
            ret =verifyAll(mid)
            if  ret:
                r=mid
            else:
                l = mid +1
            #rint(l,r,mid,ret)
        return l 
    
re =Solution().distributeCookies(cookies = [8,15,10,20,8], k = 2)
print(re)
        
        