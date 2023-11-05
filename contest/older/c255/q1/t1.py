class Solution:
    def gcd(self,a,b):
        while b:
            a,b = b,a %b
        return a

    def findGCD(self, nums):
        m1 = min(nums)
        m2 = max(nums)
        return self.gcd(m1,m2)