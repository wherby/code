
class TrieNode:
    def __init__(self):
        # 使用字典存储子节点，key 可以是 bit(0/1)，也可以是字符或任意数字
        self.children = {}
        # 记录经过该节点的所有路径中，最大的时间戳（用于区间过滤）
        self.max_idx = -1

class TimestampTrie:
    def __init__(self, max_bits=30):
        self.root = TrieNode()
        self.max_bits = max_bits

    def insert(self, val, timestamp):
        """
        向字典树插入一个值，并沿途更新时间戳。
        val: 可以是整数（按位处理），也可以是可迭代对象（如字符串）。
        """
        node = self.root
        node.max_idx = max(node.max_idx, timestamp)
        
        # 假设我们处理的是 30 位整数。如果是字符串，这里可以改为 for char in val:
        for i in range(self.max_bits, -1, -1):
            part = (val >> i) & 1
            if part not in node.children:
                node.children[part] = TrieNode()
            node = node.children[part]
            node.max_idx = max(node.max_idx, timestamp)

    def query_max_xor(self, val, min_timestamp):
        """
        在所有 timestamp >= min_timestamp 的数据中，寻找与 val 异或最大的值。
        """
        node = self.root
        # 如果整棵树最晚的更新都在窗口左侧，直接返回 0
        if node.max_idx < min_timestamp:
            return 0
        
        res = 0
        for i in range(self.max_bits, -1, -1):
            bit = (val >> i) & 1
            target = 1 - bit
            
            # 检查理想的分支（异或位）是否存在，且是否在时间窗口内
            if target in node.children and node.children[target].max_idx >= min_timestamp:
                res |= (1 << i)
                node = node.children[target]
            elif bit in node.children and node.children[bit].max_idx >= min_timestamp:
                # 理想分支不行，只能走相同位分支
                node = node.children[bit]
            else:
                # 没有任何分支满足时间戳要求，提前结束
                break
        return res