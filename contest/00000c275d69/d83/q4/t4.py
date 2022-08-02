from bisect import bisect_right
class Solution(object):
    def shortestSequence(self, rolls, k):
        """
        :type rolls: List[int]
        :type k: int
        :rtype: int
        """
        lls= [[] for _ in range(k)]
        n = len(rolls)
        for i,a in enumerate(rolls):
            lls[a-1].append(i)
        for i in range(1,n+1):
            for j in range(k):
                if len(lls[j])<i:
                    print("a")
                    return i
                ls = lls[j]
                s,e = ls[0],ls[-1]
                for a in range(k):
                    if a != j:
                        tls =lls[a]
                        idx1 =bisect_right(tls,s)
                        idx2 = bisect_right(tls,e)
                        if idx2 <i-1:
                            print("b",idx2,i)
                            return i 
                        if len(tls) - idx1<i:
                            print("c")
                            return i 
                        print(idx1,idx2,len(tls))
        return i
    
                         
                



re =Solution().shortestSequence(rolls =[1,3,3,2,1,4,1,1,2,4,1,2,2,1,1,1,1,2,2,3,4,3,3,2,1,4,4], k = 4)
#re =Solution().shortestSequence(rolls = [4,2,1,2,3,3,2,4,1], k = 4)

print(re)
