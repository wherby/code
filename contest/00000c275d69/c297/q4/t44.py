from collections import Counter
from string import ascii_lowercase
from collections import defaultdict
class Solution(object):
    def distinctNames(self, A) -> int:
        m, A = defaultdict(Counter), set(A)
        for w in A:
            m[w[0]] += Counter(x for x in ascii_lowercase if x + w[1:] not in A)
        #print(m)
        return sum(m[x][y] * m[y][x] for x in m for y in m)
    
re =Solution().distinctNames(["aaa","baa","caa","bbb","cbb","dbb"])
print(re)
