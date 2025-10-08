from functools import cache

class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        D = []
        while n:
            D.append(n % 10)
            n //= 10
        L = len(D)

        @cache
        def dfs(i, cc, A, B):
            if i == L:
                return 0 if cc else 1

            t, res = D[i], 0

            if A:
                AA = range(10) if i else range(1, 10)
            else:
                AA = (0, )

            if B:
                BB = range(10) if i else range(1, 10)
            else:
                BB = (0, )

            for da in AA:
                na = 1 if (A and da) else 0

                for db in BB:
                    nb = 1 if (B and db) else 0
                    s = da + db + cc
                    if s % 10 == t:
                        res += dfs(i + 1, s // 10, na, nb)

            return res

        return dfs(0, 0, 1, 1)