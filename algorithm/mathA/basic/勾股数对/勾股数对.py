

from math import gcd
class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        u = 3
        while u * u < n * 2:
            v = 1
            while v < u and u * u + v * v <= n * 2:
                if gcd(u, v) == 1:
                    ans += n * 2 // (u * u + v * v)
                    if u ==7 and v ==3:
                        print(u,v)
                v += 2
            u += 2
        return ans * 2  # (a,b,c) 和 (b,a,c) 各算一次

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/count-square-sum-triples/solutions/869409/go-yu-chu-li-you-hua-by-endlesscheng-61mj/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

re =Solution().countTriples(100)
print(re)