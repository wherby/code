import math
class Solution(object):
    def countDifferentSubsequenceGCDs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        g = [0]* 200002
        for n in nums:
            for i in range(1,int(math.sqrt(n)+1)):
                if n %i ==0:
                    if g[i] ==0:
                        g[i] =n
                    else:
                        g[i] = math.gcd(g[i],n)
                    if n//i != i:
                        t = n//i
                        if g[t] ==0:
                            g[t] =n
                        else:
                            g[t] = math.gcd(g[t],n)
        cnt =0
        for i in range(1,200002):
            if g[i] == i:
                cnt +=1
        return cnt