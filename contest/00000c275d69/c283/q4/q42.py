import math
class Solution:
    def replaceNonCoprimes(self, nums):
        def lcm(x, y) :
            return x * y // math.gcd(x, y)

        vs = []
        for t in nums :
            vs.append(t)
            while len(vs) > 1 and math.gcd(vs[-1], vs[-2]) > 1 :
                new = vs[-1] * vs[-2] // math.gcd(vs[-1], vs[-2])
                vs[-2] = new
                vs.pop(-1)
        return vs