from itertools import count

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        f = [[0]*(k+1) for _ in range(n+1)]
        for i in count(1):
            for j in range(1,k+1):
                f[i][j] = f[i-1][j-1] +f[i-1][j] +1
            if f[i][j] >= n:
                return i