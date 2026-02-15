
class TimestampTrie:
    def __init__(self, max_bits=31):
        # 使用数组存储，避免频繁的对象实例化
        # 0 号节点是 root
        self.max_bits = max_bits
        self.trie = [[-1, -1]]  # trie[u][0/1] 记录子节点索引
        self.max_idx = [-1]      # max_idx[u] 记录经过该节点的最大时间戳
    
    def insert(self, val, timestamp):
        u = 0
        self.max_idx[u] = max(self.max_idx[u], timestamp)
        for i in range(self.max_bits, -1, -1):
            bit = (val >> i) & 1
            if self.trie[u][bit] == -1:
                self.trie[u][bit] = len(self.trie)
                self.trie.append([-1, -1])
                self.max_idx.append(-1)
            u = self.trie[u][bit]
            self.max_idx[u] = max(self.max_idx[u], timestamp)
            
    def query_max_xor(self, val, min_timestamp):
        """
        在所有 timestamp >= min_timestamp 的前缀中，
        寻找与 val 异或值最大的结果。
        """
        if self.max_idx[0] < min_timestamp:
            return 0
        
        u = 0
        res = 0
        for i in range(self.max_bits, -1, -1):
            bit = (val >> i) & 1
            target = 1 - bit
            
            # 核心逻辑：只有子节点存在且其最新的时间戳满足窗口要求，才往该分支走
            target_node = self.trie[u][target]
            if target_node != -1 and self.max_idx[target_node] >= min_timestamp:
                res |= (1 << i)
                u = target_node
            else:
                u = self.trie[u][bit]
                if u == -1: break # 正常情况下 insert(0,0) 后不会发生
        return res