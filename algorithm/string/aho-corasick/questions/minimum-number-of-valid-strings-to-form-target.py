#  AC自动机 https://oi-wiki.org/string/ac-automaton/#__tabbed_1_2
from typing import List, Tuple, Optional
from collections import defaultdict,deque

# 从根到 node 的字符串是某个（某些）words[i] 的前缀
class Node:
    __slots__ = 'son', 'fail', 'len'

    def __init__(self, len=0):
        self.son = [None] * 26
        self.fail = None  # 当 cur.son[i] 不能匹配 target 中的某个字符时，cur.fail.son[i] 即为下一个待匹配节点（等于 root 则表示没有匹配）
        self.len = len  # 从根到 node 的字符串的长度，也是 node 在 trie 中的深度

class AhoCorasick:
    def __init__(self):
        self.root = Node()

    def put(self, s: str) -> None:
        cur = self.root
        for b in s:
            b = ord(b) - ord('a')
            if cur.son[b] is None:
                cur.son[b] = Node(cur.len + 1)
            cur = cur.son[b]

    def build_fail(self) -> None:
        self.root.fail = self.root
        q = deque()
        for i, son in enumerate(self.root.son):
            if son is None:
                self.root.son[i] = self.root
            else:
                son.fail = self.root  # 第一层的失配指针，都指向根节点 ∅
                q.append(son)
        # BFS
        while q:
            cur = q.popleft()
            for i, son in enumerate(cur.son):
                if son is None:
                    # 虚拟子节点 cur.son[i]，和 cur.fail.son[i] 是同一个
                    # 方便失配时直接跳到下一个可能匹配的位置（但不一定是某个 words[k] 的最后一个字母）
                    cur.son[i] = cur.fail.son[i]
                    continue
                son.fail = cur.fail.son[i]  # 计算失配位置
                q.append(son)

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        ac = AhoCorasick()
        for w in words:
            ac.put(w)
        ac.build_fail()

        n = len(target)
        f = [0] * (n + 1)
        cur = root = ac.root
        for i, c in enumerate(target, 1):
            # 如果没有匹配相当于移动到 fail 的 son[c]
            cur = cur.son[ord(c) - ord('a')]
            # 没有任何字符串的前缀与 target[..i] 的后缀匹配
            if cur is root:
                return -1
            f[i] = f[i - cur.len] + 1
        return f[n]

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-number-of-valid-strings-to-form-target-ii/solutions/2917929/ac-zi-dong-ji-pythonjavacgo-by-endlessch-hcqk/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    
re = Solution().minValidStrings( words = ["abababab","ab"], target = "ababaababa")
print(re)