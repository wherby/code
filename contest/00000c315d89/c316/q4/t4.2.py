# https://leetcode.com/contest/weekly-contest-316/problems/minimum-number-of-operations-to-make-arrays-similar/
# https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/solutions/2734189/c-python-sort-odds-and-evens/

from typing import List, Tuple, Optional



class Solution:
    def makeSimilar(self, A, B):
        A1 = sorted(a for a in A if a % 2)
        B1 = sorted(a for a in B if a % 2)
        A2 = sorted(a for a in A if a % 2 == 0)
        B2 = sorted(a for a in B if a % 2 == 0)
        res1 = sum(abs(a - b) // 2 for a,b in zip(A1, B1))
        res2 = sum(abs(a - b) // 2 for a,b in zip(A2, B2))
        return (res1 + res2) // 2