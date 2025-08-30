# Finding the lexicographically smallest string of length  L contains K strings 
# https://cp-algorithms.com/string/aho_corasick.html#finding-the-lexicographically-smallest-string-of-length-l-containing-k-strings

import collections

class Vertex:
    def __init__(self):
        self.next_nodes = {}
        self.parent = -1
        self.parent_char = ''
        self.link = -1
        self.go_nodes = {}
        self.output_mask = 0

class AhoCorasick:
    def __init__(self, patterns: list):
        self.patterns = patterns
        self.trie = [Vertex()]
        self._go_cache = {}
        self.all_found_mask = (1 << len(patterns)) - 1
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
            self.trie[v].output_mask |= (1 << i)

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
        for v in range(len(self.trie)):
            self._get_link(v)
            for ch_code in range(ord('a'), ord('z') + 1):
                ch = chr(ch_code)
                self.trie[v].go_nodes[ch] = self._go(v, ch)
        
        for v in range(len(self.trie)):
            if self.trie[v].link != -1:
                link_node = self.trie[v].link
                self.trie[v].output_mask |= self.trie[link_node].output_mask

class SmallestStringSolver:
    def __init__(self, patterns: list):
        self.ac = AhoCorasick(patterns)
        self.num_patterns = len(patterns)
        self.target_k = 0
        self.target_L = 0
        self.memo = {}

    def solve(self, length: int, k_matches: int) -> str:
        self.target_L = length
        self.target_k = k_matches
        
        # 使用 memoization 缓存状态 (node, length, mask)
        self.memo = {}
        
        # 结果将由 BFS 保证最短，DFS 保证字典序最小
        path = self._dfs(0, 0, 0)
        
        if path is not None:
            return "".join(path)
        else:
            return "No solution found"

    def _dfs(self, current_node: int, current_length: int, current_mask: int) -> list:
        # 检查是否已经到达目标状态
        matched_count = bin(current_mask).count('1')
        if current_length == self.target_L and matched_count == self.target_k:
            return []

        # 检查是否超出界限
        if current_length > self.target_L or matched_count > self.target_k:
            return None
        
        # 使用 memoization
        state = (current_node, current_length, current_mask)
        if state in self.memo:
            return self.memo[state]

        # 遍历所有可能的下一个字符 (按字典序)
        for ch_code in range(ord('a'), ord('z') + 1):
            ch = chr(ch_code)
            next_node = self.ac.trie[current_node].go_nodes[ch]

            # 更新掩码：将新节点上的匹配掩码与当前掩码合并
            next_mask = current_mask | self.ac.trie[next_node].output_mask
            
            # 递归调用
            sub_path = self._dfs(next_node, current_length + 1, next_mask)
            
            if sub_path is not None:
                result = [ch] + sub_path
                self.memo[state] = result
                return result

        self.memo[state] = None
        return None

# 使用示例
if __name__ == "__main__":
    patterns = ["ab", "bc", "c"]
    length = 4
    k_matches = 2

    solver = SmallestStringSolver(patterns)
    result = solver.solve(length, k_matches)
    
    print(f"模式串: {patterns}")
    print(f"要找的字符串长度: {length}, 匹配数: {k_matches}")
    print(f"满足条件的最小字典序字符串是: {result}")

    print("-" * 20)

    patterns_2 = ["abc", "bc", "dda","ad"]
    length_2 = 10
    k_matches_2 = 3
    solver_2 = SmallestStringSolver(patterns_2)
    result_2 = solver_2.solve(length_2, k_matches_2)
    print(f"模式串: {patterns_2}")
    print(f"要找的字符串长度: {length_2}, 匹配数: {k_matches_2}")
    print(f"满足条件的最小字典序字符串是: {result_2}")