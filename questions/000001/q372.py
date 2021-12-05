import math
class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        res = 1
        mod = 1337
        a= a%mod
        for x in b:
            res =(pow(res,10))%mod
            res = (res *pow(a,x)) % mod
        return res
    
    def superPow2(self, a: int, b: list[int]) -> int:
        MOD = 1337
        ans = 1
        for e in b:
            ans = pow(ans, 10, MOD) * pow(a, e, MOD) % MOD
        return ans


            
re =Solution().superPow(2147483647,[2,0,0])
print(re)
print(math.pow(19,19)%1337)
print(pow(19,19)%1337)
# a**523 = ((a**5)**10 *(a**2)) **10  * (a**3)  