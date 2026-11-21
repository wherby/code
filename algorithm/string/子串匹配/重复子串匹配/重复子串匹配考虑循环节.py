# https://leetcode.cn/problems/repeated-string-match-ii/submissions/
from typing import List, Tuple, Optional


class Solution:
    def repeatedStringMatch(self, a: str, b: str, x: int, y: int) -> bool:
        n, m = len(a), len(b)
        if m * y > n * x:
            return False
        if x == 1:
            return (b * y) in a

        if y == 1:
            k = min(x, (m + n - 1) // n + 2)
            A_check = a * k
            start = 0
            while True:
                idx = A_check.find(b, start)
                if idx == -1:
                    return False
                if idx + m <= n * x:
                    return True
                start = idx + 1
            return False

        def get_primitive_root(s: str) -> str:
            L = len(s)
            lps = [0] * L
            length = 0
            i = 1
            while i < L:
                if s[i] == s[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            k = L - lps[-1]
            if L % k == 0:
                return s[:k]
            return s

        u_a = get_primitive_root(a)
        u_b = get_primitive_root(b)
        l_a, l_b = len(u_a), len(u_b)

        if l_a != l_b:
            return False

        if u_b not in (u_a + u_a):
            return False

        extended_a = u_a * ((m + l_a - 1) // l_a + 2)
        found_offset = extended_a.find(b)

        if found_offset == -1:
            return False

        total_len_b = m * y
        total_len_a = n * x

        if found_offset + total_len_b > total_len_a:
            return False

        return True


re = Solution().repeatedStringMatch(a="abc", b="bc", x=2, y=3)
print(re)
