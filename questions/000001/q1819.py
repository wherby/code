import math
class Solution:
    def countDifferentSubsequenceGCDs(self, nums) -> int:
        mx = max(nums)
        st = set(nums)
        cnt =0

        for i in range(1,mx+1):
            gcd = 0
            for j in range(i,mx+1,i):
                if j in st:
                    if gcd ==0:
                        gcd = j
                    else:
                        gcd = math.gcd(j,gcd)
                    if gcd == i:
                        cnt +=1
                        break
        return cnt 
    
re =Solution().countDifferentSubsequenceGCDs(nums = [6,10,3]) 
print(re)
            