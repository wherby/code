

# 1 到n 的字典序排列
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = [0] * n
        num = 1
        for i in range(n):
            ans[i] = num
            if num * 10 <= n:
                num *= 10
            else:
                while num % 10 == 9 or num + 1 > n:
                    num //= 10
                num += 1
        return ans

# [仿射函数，把四则运算转换为Combination](../segmentTree/仿射函数)
[线段树处理四则运算](../codeforce/技巧/四则运算统一为加法.py)