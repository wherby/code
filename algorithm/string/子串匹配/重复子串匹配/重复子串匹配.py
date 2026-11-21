class Solution:
    def repeatedStringMatch(self, a: str, b: str, x: int, y: int) -> bool:
        n, m = len(a), len(b)
        len_a, len_b = n * x, m * y
        if len_b > len_a:
            return False

        firsts = min(lcm(n, m), len_b)
        for start in range(min(n, len_a - len_b + 1)):
            # 判断 B 是否为 A[start:] 的前缀
            # 只需比较前 firsts 个字母
            if all(a[(start + i) % n] == b[i % m] for i in range(firsts)):
                return True
        return False


# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/repeated-string-match-ii/solutions/4054618/bao-li-pythonjavacgo-by-endlesscheng-efnn/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
