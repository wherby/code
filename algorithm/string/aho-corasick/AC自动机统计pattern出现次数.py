# https://leetcode.cn/problems/number-of-strings-that-appear-as-substrings-in-word/description/?envType=daily-question&envId=2026-06-29
# 给你一个字符串数组 patterns 和一个字符串 word ，统计 patterns 中有多少个字符串是 word 的子字符串。返回字符串数目。
# algorithm/string/aho-corasick/AC自动机.md
from typing import List, Tuple, Optional
from collections import defaultdict,deque
class Node:
    __slots__ = 'son', 'fail', 'last', 'cnt'

    def __init__(self):
        self.son = [None] * 26
        self.fail = None  # 当 node.son[i] 失配时，node.fail.son[i] 即为下一个待匹配节点（等于 root 则表示没有匹配）
        self.last = None  # 后缀链接（suffix link），用来快速跳到一定是某个模式串末尾的节点（等于 root 则表示匹配结束）
        self.cnt = 0  # node 是 cnt 个模式串的末尾


class AhoCorasick:
    def __init__(self):
        self.root = Node()

    # 把模式串 pattern 插入 AC 自动机（代码和字典树一样）
    def put(self, pattern: str) -> None:
        cur = self.root
        for ch in pattern:
            i = ord(ch) - ord('a')
            if cur.son[i] is None:
                cur.son[i] = Node()
            cur = cur.son[i]
        cur.cnt += 1

    # BFS，构建 AC 自动机的 fail 和 last，方便快速查询
    def build_fail(self) -> None:
        self.root.fail = self.root.last = self.root

        q = deque()
        for i, son in enumerate(self.root.son):
            if son is None:
                self.root.son[i] = self.root
                continue
            son.fail = son.last = self.root  # 第一层的 fail 都指向根节点
            q.append(son)

        # BFS
        while q:
            cur = q.popleft()
            for i, son in enumerate(cur.son):
                if son is None:
                    # 把虚拟子节点 cur.son[i] 设置为 cur.fail.son[i]
                    # 方便失配时直接跳到下一个可能匹配的位置（但不一定是某个模式串的末尾）
                    cur.son[i] = cur.fail.son[i]
                    continue
                son.fail = cur.fail.son[i]  # 计算失配位置
                # 沿着 last 往上走，可以直接跳到一定是某个模式串末尾的节点（如果跳到 root 表示匹配结束）
                son.last = son.fail if son.fail.cnt else son.fail.last
                q.append(son)

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ac = AhoCorasick()
        for pattern in patterns:
            ac.put(pattern)
        ac.build_fail()

        ord_a = ord('a')
        cur = ac.root
        ans = 0
        
        # 用一个集合记录哪些【有效单词节点】已经被统计过了
        visited = set()
        
        for ch in word:
            cur = cur.son[ord(ch) - ord_a]
            match_node = cur
            
            # 沿着 last 链向上找，直到根节点，或者遇到已经访问过的节点
            while match_node != ac.root and match_node not in visited:
                if match_node.cnt > 0:
                    ans +=  match_node.cnt
                    visited.add(match_node) # 标记该单词已找到
                
                # 继续跳向下一个有效单词节点
                match_node = match_node.last
                
        return ans