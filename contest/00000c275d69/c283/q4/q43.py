import math
class Solution(object):
    def replaceNonCoprimes(self, nums):
        res =[]
        while len(nums)>0:
            if len(res) >0:
                a = nums.pop()
                b = res.pop()
                if math.gcd(a,b) ==1:
                    res.append(b)
                    res.append(a)
                else:
                    nums.append(a*b // math.gcd(a,b))
            else:
                res.append(nums.pop())
        return res[::-1]


re = Solution().replaceNonCoprimes([6,4,3,2,7,6,2])
print(re)