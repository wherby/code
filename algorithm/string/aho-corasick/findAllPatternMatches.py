# Find all strings from a given set in a text
# https://cp-algorithms.com/string/aho_corasick.html
# 利用 出口链接（exit link） 实现了在寻找 abc的同时找到bc
# 出口链接的作用
#出口链接正是为了解决这个问题而生。它不是指向最长真后缀，而是直接指向沿着失败链接路径能遇到的第一个有匹配的节点。
#想象一下，你有一条通向山顶的路（失败链接），但路上有很多可以休息的站点。出口链接就像一条捷径，直接带你从当前位置到下一个能找到“宝藏”的站点，而不需要一个个地走。

import collections

class Vertex:
    def __init__(self):
        self.next_nodes = {}
        self.parent = -1
        self.parent_char = ''
        self.link = -1
        self.go_nodes = {}
        self.output_patterns = []  # 存储在此节点结束的模式串的索引
        self.exit_link = -1       # 新增：出口链接

class AhoCorasick:
    def __init__(self, patterns: list):
        self.patterns = patterns
        self.trie = [Vertex()]
        self._go_cache = {}
        self._build_trie()
        self._build_automaton()

    def _build_trie(self):
        for i, s in enumerate(self.patterns):
            v = 0
            for ch in s:
                if ch not in self.trie[v].next_nodes:
                    self.trie[v].next_nodes[ch] = len(self.trie)
                    self.trie.append(Vertex())
                    self.trie[-1].parent = v
                    self.trie[-1].parent_char = ch
                v = self.trie[v].next_nodes[ch]
            self.trie[v].output_patterns.append(i)

    def _get_link(self, v: int) -> int:
        if self.trie[v].link == -1:
            if v == 0 or self.trie[v].parent == 0:
                self.trie[v].link = 0
            else:
                parent_link = self._get_link(self.trie[v].parent)
                self.trie[v].link = self._go(parent_link, self.trie[v].parent_char)
        return self.trie[v].link

    def _go(self, v: int, ch: str) -> int:
        if (v, ch) in self._go_cache:
            return self._go_cache[(v, ch)]
        
        if ch in self.trie[v].next_nodes:
            result = self.trie[v].next_nodes[ch]
        else:
            result = 0 if v == 0 else self._go(self._get_link(v), ch)
        
        self._go_cache[(v, ch)] = result
        return result

    def _build_automaton(self):
        queue = collections.deque()
        for ch, next_node in self.trie[0].next_nodes.items():
            self.trie[next_node].link = 0
            queue.append(next_node)
        
        # 预计算所有节点的失败链接和转移
        for v in range(len(self.trie)):
            self._get_link(v)
            for ch_code in range(ord('a'), ord('z') + 1):
                ch = chr(ch_code)
                self.trie[v].go_nodes[ch] = self._go(v, ch)
        
        # 构建出口链接
        for v in range(1, len(self.trie)):
            link_node = self.trie[v].link
            if self.trie[link_node].output_patterns:
                self.trie[v].exit_link = link_node
            else:
                self.trie[v].exit_link = self.trie[link_node].exit_link


    def find_all_matches(self, text: str) -> list:
            """
            在文本中查找所有模式串的出现。
            返回一个包含 (模式索引, 结束位置) 元组的列表。
            """
            results = []
            v = 0
            for i, ch in enumerate(text):
                if ch not in self.trie[v].go_nodes:
                    continue # 如果字符不在字母表范围内，直接跳过
                
                v = self.trie[v].go_nodes[ch]
                current_node = v

                # 使用出口链接高效地查找所有匹配
                while current_node != -1:
                    # 如果当前节点是输出节点，记录匹配
                    for pattern_index in self.trie[current_node].output_patterns:
                        results.append((pattern_index, i))
                    
                    # 沿着出口链接继续查找
                    current_node = self.trie[current_node].exit_link
            
            return results

# 使用示例
if __name__ == "__main__":
    patterns = ["he", "she", "hers", "his"]
    text = "ushers"

    ac = AhoCorasick(patterns)
    matches = ac.find_all_matches(text)

    print("在文本中找到以下匹配:")
    for pattern_index, end_pos in matches:
        pattern = ac.patterns[pattern_index]
        start_pos = end_pos - len(pattern) + 1
        print(f"模式 '{pattern}' 在索引 {start_pos} 到 {end_pos} 处匹配")

    # 另一个示例
    patterns_2 = ["abc", "bc"]
    text_2 = "dabc"
    ac2 = AhoCorasick(patterns_2)
    matches_2 = ac2.find_all_matches(text_2)

    print("\n在文本中找到以下匹配:")
    for pattern_index, end_pos in matches_2:
        pattern = ac2.patterns[pattern_index]
        start_pos = end_pos - len(pattern) + 1
        print(f"模式 '{pattern}' 在索引 {start_pos} 到 {end_pos} 处匹配")