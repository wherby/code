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