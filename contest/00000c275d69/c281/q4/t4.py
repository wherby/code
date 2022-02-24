import math

class Solution(object):
    def coutPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def gcd(a,b):
            while b:
                a,b = b,a %b
            return a
        ls= [0]*110000
        sm = 0
        for a in nums:
            g1 = gcd(k,a)
            re = k // g1
            sm += ls[re]
            t = int(math.sqrt(g1)) 
            for j in range(1,t+1):
                if g1 %j ==0:
                    ls[j] +=1
                    if g1//j != j:
                        ls[g1//j]+=1
        return sm




        