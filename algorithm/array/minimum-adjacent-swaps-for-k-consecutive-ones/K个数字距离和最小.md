

    def minMoves(self, A, k):
        A = [i for i, a in enumerate(A) if a]
        n = len(A)
        B = [0] * (n + 1)
        res = float('inf')
        for i in xrange(n):
            B[i + 1] = B[i] + A[i]
        for i in xrange(len(A) - k + 1):
            res = min(res, B[i + k] - B[k / 2 + i] - B[(k + 1) / 2 + i] + B[i])
        res -= (k / 2) * ((k + 1) / 2)
        return res

```https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/solutions/987347/java-c-python-solution/

I worked out how this magic works
B[i + k] - B[k / 2 + i] - B[(k + 1) / 2 + i] + B[i])

example indices (A):
[0 3 5 6 7 9 10]
mid = 6
sum before mid => (6 - 6 - 0) + (6 - 3 - 1) + (6 - 5 - 2) + (6 - 0 - 3)
=> 6 * 4 - (0 + 3 + 5 + 6) - (0 + 1 + 2 + 3)

sum after mid => (6 - 6 - 0) + (7 - 6 - 1) + (9 - 6 - 2) + (10 - 6 - 3)
=> (6 + 7 + 9 + 10) - 6 * 4 - (0 + 1 + 2 + 3)

before + after => (6 + 7 + 9 + 10) - (0 + 3 + 5 + 6) - 2 * (1+2+3)
=> A[3]->A[6] - A[0]->A[3] - 2 * (3)(3+1) / 2
=> (B[7] - B[3]) - (B[4] - B[0]) - (k//2)*((k+1)//2)
```