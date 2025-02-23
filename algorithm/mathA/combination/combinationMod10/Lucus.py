# https://oi-wiki.org/math/number-theory/lucas/
# Lucas 定理用于求解大组合数取模的问题，其中模数必须为素数。正常的组合数运算可以通过递推公式求解（详见 排列组合），但当问题规模很大，而模数是一个不大的质数的时候，就不能简单地通过递推求解来得到答案，需要用到 Lucas 定理。
class Solution:
    
    def hasSameDigits(self, s: str) -> bool:
        def comb_mod(n: int, k: int, p: int) -> int:
            """使用 Lucas 定理计算 C(n, k) mod p，其中 p 为质数"""
            if k < 0 or k > n:
                return 0
            result = 1
            while n > 0 or k > 0:
                ni = n % p
                ki = k % p
                if ki > ni:
                    return 0
                # 计算 C(ni, ki) mod p
                numerator = 1
                denominator = 1
                for i in range(ki):
                    numerator = numerator * (ni - i) % p
                    denominator = denominator * (i + 1) % p
                # 分母的逆元（费马小定理）
                denominator_inv = pow(denominator, p - 2, p)
                result = result * (numerator * denominator_inv % p) % p
                n = n // p
                k = k // p
            return result
        
        def crt(a2: int, a5: int) -> int:
            """中国剩余定理合并模 2 和模 5 的结果"""
            for x in range(10):
                if x % 2 == a2 and x % 5 == a5:
                    return x
            return 0
        def comb_mod_10(n: int, k: int) -> int:
            """计算 C(n, k) mod 10"""
            c2 = comb_mod(n, k, 2)
            c5 = comb_mod(n, k, 5)
            return crt(c2, c5)
        nums = list(map(int, s))
        n = len(nums)
        if n == 2:
            return nums[0] == nums[1]
        m = n - 2  # 操作次数
        result1, result2 = 0, 0
        for i in range(n):
            # 计算第一个结果的权重 C(m, i) mod 10
            c1 = comb_mod_10(m, i)
            # 计算第二个结果的权重 C(m, i-1) mod 10
            c2 = comb_mod_10(m, i - 1)
            result1 = (result1 + nums[i] * c1) % 10
            result2 = (result2 + nums[i] * c2) % 10
        return result1 == result2