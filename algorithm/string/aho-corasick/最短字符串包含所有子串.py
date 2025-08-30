# https://cp-algorithms.com/string/aho_corasick.html
# # 传播 output_mask 也用了 出口链接（exit link） 思想
# Finding the shortest string containing all given strings
import collections

class Vertex:
    def __init__(self):
        self.next_nodes = {}
        self.parent = -1
        self.parent_char = ''
        self.link = -1
        self.go_nodes = {}
        self.output_mask = 0  # 使用整数掩码来表示在此节点结束的模式串集合

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
        # 预计算所有节点的失败链接和转移
        for v in range(len(self.trie)):
            self._get_link(v)
            for ch_code in range(ord('a'), ord('z') + 1):
                ch = chr(ch_code)
                self.trie[v].go_nodes[ch] = self._go(v, ch)
        
        # 传播 output_mask
        for v in range(1, len(self.trie)):
            link_node = self.trie[v].link
            self.trie[v].output_mask |= self.trie[link_node].output_mask


class ShortestSuperstringSolver:
    def __init__(self, patterns: list):
        self.ac = AhoCorasick(patterns)
        self.num_patterns = len(patterns)
        self.all_found_mask = (1 << self.num_patterns) - 1

    def find_shortest_superstring(self) -> str:
        queue = collections.deque()
        visited = set()

        # 初始状态: (根节点, 掩码0, 空字符串)
        start_state = (0, 0, "")
        queue.append(start_state)
        visited.add((0, 0))

        while queue:
            current_node, current_mask, current_path = queue.popleft()

            # 检查是否达到目标状态
            if current_mask == self.all_found_mask:
                return current_path

            # 遍历所有可能的下一个字符
            for ch_code in range(ord('a'), ord('z') + 1):
                ch = chr(ch_code)
                next_node = self.ac.trie[current_node].go_nodes[ch]
                
                # 更新掩码：将新节点上的匹配掩码与当前掩码合并
                next_mask = current_mask | self.ac.trie[next_node].output_mask
                
                # 如果这个状态是第一次访问，则加入队列
                if (next_node, next_mask) not in visited:
                    visited.add((next_node, next_mask))
                    next_path = current_path + ch
                    queue.append((next_node, next_mask, next_path))
        
        return "No solution found"

# 使用示例
if __name__ == "__main__":
    patterns = ["ab", "bc", "ca"]
    solver = ShortestSuperstringSolver(patterns)
    result = solver.find_shortest_superstring()
    print(f"模式串: {patterns}")
    print(f"最短超串是: {result}")
    
    print("-" * 20)

    patterns_2 = ["abc", "bca", "cab"]
    solver_2 = ShortestSuperstringSolver(patterns_2)
    result_2 = solver_2.find_shortest_superstring()
    print(f"模式串: {patterns_2}")
    print(f"最短超串是: {result_2}")