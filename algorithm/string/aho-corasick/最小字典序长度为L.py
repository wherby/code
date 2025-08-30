
# 你描述的问题是如何找到一个给定长度 L 的、词典序最小的、且不包含任何给定模式串的字符串。这个问题可以通过构建 Aho-Corasick 自动机来高效解决。🎯
# Aho-Corasick 自动机与问题转换
# 首先，我们把所有给定的模式串构建成一个 Aho-Corasick 自动机。这个自动机是一个特殊的 Trie 树，每个节点代表一个字符串前缀，并且它还包含失败链接（failure link）。失败链接的作用是，
# 当我们无法沿着当前路径继续匹配时，可以快速跳转到另一个节点，这个节点代表着当前前缀的最长真后缀，从而避免重新从头开始匹配。
# 自动机中的一些节点被标记为 "输出"（output）节点，这意味着从根节点到这些节点的路径正好构成一个完整的模式串。在你的问题中，我们不能包含任何模式串，
# 这意味着我们不能进入这些 "输出" 节点。此外，如果某个节点通过它的失败链接指向一个 "输出" 节点，这也意味着从根到当前节点的路径包含一个模式串作为后缀。因此，
# 所有直接或间接地通过失败链接连接到 "输出" 节点的节点，都应该被视为**"坏"（bad）节点**，我们不允许进入。
# https://cp-algorithms.com/string/aho_corasick.html
# 用bad node 隔绝图中的边界


import collections

class Vertex:
    """Aho-Corasick 自动机中的一个节点。"""
    def __init__(self, parent=-1, parent_char=''):
        self.next_nodes = {}
        self.output = False
        self.parent = parent
        self.parent_char = parent_char
        self.link = -1
        self.go_nodes = {}

class AhoCorasick:
    """
    一个用于构建和查询 Aho-Corasick 自动机的主类。
    """
    def __init__(self, patterns):
        self.trie = [Vertex()]
        self._go_cache = {}
        self.bad_nodes = set()

        for pattern in patterns:
            self.add_string(pattern)

        self._build_automaton()

    def add_string(self, s: str):
        """向自动机中添加一个模式串。"""
        v = 0
        for ch in s:
            if ch not in self.trie[v].next_nodes:
                self.trie[v].next_nodes[ch] = len(self.trie)
                self.trie.append(Vertex(v, ch))
            v = self.trie[v].next_nodes[ch]
        self.trie[v].output = True

    def _get_link(self, v: int) -> int:
        """递归地计算失败链接。"""
        if self.trie[v].link == -1:
            if v == 0 or self.trie[v].parent == 0:
                self.trie[v].link = 0
            else:
                parent_link = self._get_link(self.trie[v].parent)
                self.trie[v].link = self._go(parent_link, self.trie[v].parent_char)
        return self.trie[v].link

    def _go(self, v: int, ch: str) -> int:
        """计算转移。"""
        if (v, ch) in self._go_cache:
            return self._go_cache[(v, ch)]

        if ch in self.trie[v].next_nodes:
            result = self.trie[v].next_nodes[ch]
        else:
            result = 0 if v == 0 else self._go(self._get_link(v), ch)
        
        self._go_cache[(v, ch)] = result
        return result

    def _build_automaton(self):
        """
        构建完整的 Aho-Corasick 自动机，并标记所有坏节点。
        """
        queue = collections.deque()
        
        # 初始化根节点的子节点队列
        for ch, next_node in self.trie[0].next_nodes.items():
            self.trie[next_node].link = 0
            queue.append(next_node)
        
        # 标记所有直接的 output 节点为坏节点
        for v in range(len(self.trie)):
            if self.trie[v].output:
                self.bad_nodes.add(v)

        # BFS 遍历所有节点，将通过失败链接到达 output 节点的节点标记为坏节点
        # 这一步必须在所有失败链接都计算完之后进行，或者在 BFS 过程中动态处理
        for v in range(len(self.trie)):
            if v in self.bad_nodes:
                continue
            
            link_node = self._get_link(v)
            if link_node in self.bad_nodes:
                self.bad_nodes.add(v)

        # 预计算所有可能的转移，以备查询时使用
        for v in range(len(self.trie)):
            for ch_code in range(ord('a'), ord('z') + 1):
                ch = chr(ch_code)
                self.trie[v].go_nodes[ch] = self._go(v, ch)
    
    def find_smallest_non_matching(self, length: int) -> str:
        """
        找到给定长度的、词典序最小的、不匹配任何模式的字符串。
        使用 DFS 实现。
        """
        path = []
        
        def dfs(current_node: int, current_length: int) -> bool:
            if current_length == length:
                return True

            for ch_code in range(ord('a'), ord('z') + 1):
                ch = chr(ch_code)
                next_node = self.trie[current_node].go_nodes[ch]
                
                # 检查下一个节点是否在坏节点集合中
                if next_node not in self.bad_nodes:
                    path.append(ch)
                    if dfs(next_node, current_length + 1):
                        return True
                    path.pop()  # 回溯
            return False

        if dfs(0, 0):
            return "".join(path)
        else:
            return "No such string exists"

# 使用示例
patterns = ["aa", "ab", "ac","ad","aea","bae"]
length = 5

ac = AhoCorasick(patterns)
result = ac.find_smallest_non_matching(length)
print(f"模式串: {patterns}")
print(f"要找的字符串长度: {length}")
print(f"词典序最小的不匹配字符串是: {result}")