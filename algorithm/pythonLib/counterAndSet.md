# set diff and counter
https://leetcode-cn.com/problems/uncommon-words-from-two-sentences/submissions/

```
import collections
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ls11 = collections.Counter(s1.split(" "))
        ls21 = collections.Counter(s2.split(" "))
        ls1 = set(s1.split(" "))
        ls2 = set(s2.split(" "))
        res = ls1.symmetric_difference(ls2)
        res =list(res)
        print(res)
        res = filter(lambda x: ls11[x] ==1 or ls21[x] ==1,res)
        return list(res)
```

## Counter
https://leetcode.cn/submissions/detail/324447394/
class Solution(object):
    def distinctNames(self, A) -> int:
        m, A = defaultdict(Counter), set(A)
        for w in A:
            m[w[0]] += Counter(x for x in ascii_lowercase if x + w[1:] not in A)
        return sum(m[x][y] * m[y][x] for x in m for y in m)

>>> a = Counter(x for x in "abc")
>>> a
Counter({'a': 1, 'b': 1, 'c': 1})