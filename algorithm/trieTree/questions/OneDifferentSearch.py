# https://leetcode.cn/problems/implement-magic-dictionary/description/?envType=daily-question&envId=2024-08-12
# 
from typing import List, Tuple, Optional
class Trie:
    __slots__ = "children", "is_end"

    def __init__(self):
        self.children: List[Optional[Trie]] = [None] * 26
        self.is_end = False

    def insert(self, w: str) -> None:
        node = self
        for c in w:
            idx = ord(c) - ord("a")
            if node.children[idx] is None:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.is_end = True

    def search(self, w: str) -> bool:
        def dfs(i: int, node: Optional[Trie], diff: int) -> bool:
            if i == len(w):
                return diff == 1 and node.is_end
            j = ord(w[i]) - ord("a")
            if node.children[j] and dfs(i + 1, node.children[j], diff):
                return True
            return diff == 0 and any(
                node.children[k] and dfs(i + 1, node.children[k], 1)
                for k in range(26)
                if k != j
            )

        return dfs(0, self, 0)


class MagicDictionary:
    def __init__(self):
        self.trie = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for w in dictionary:
            self.trie.insert(w)

    def search(self, searchWord: str) -> bool:
        return self.trie.search(searchWord)

so =  MagicDictionary()
so.buildDict(["aabc","babc"])
print(so.search("aabc"))


#作者：ylb
#链接：https://leetcode.cn/problems/implement-magic-dictionary/solutions/2877189/python3javacgotypescript-yi-ti-yi-jie-qi-z5ve/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。