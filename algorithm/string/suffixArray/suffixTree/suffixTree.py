# https://oi-wiki.org/string/suffix-tree/
# https://cp-algorithms.com/string/suffix-tree-ukkonen.html

class Node:
    """
    后缀树中的节点，代表一个状态。
    l, r: 边上的子串在原始字符串中的左右边界。
    par: 父节点索引。
    link: 后缀链接。
    next: 指向子节点的字典，键是字符，值是节点索引。
    """
    def __init__(self, l=0, r=0, par=-1):
        self.l = l
        self.r = r
        self.par = par
        self.link = -1
        self.next = {}

    def get_len(self, current_pos):
        """计算边的长度，如果r是全局位置，则需要用当前位置来计算长度"""
        return self.r - self.l

class State:
    """
    Ukkonen 算法中的活动点（Active Point）。
    v: 活动节点索引。
    pos: 在从 v 发出的边上的位置。
    """
    def __init__(self, v, pos):
        self.v = v
        self.pos = pos

class SuffixTree:
    """
    一个实现了 Ukkonen 算法的后缀树构建器。
    """
    def __init__(self, s):
        self.s = s
        self.n = len(s)
        self.tree = [Node()]
        self.sz = 1
        self.ptr = State(0, 0)
    
    def get_node(self, index):
        """根据索引返回节点对象"""
        if index == -1:
            return None
        return self.tree[index]

    def _go(self, st, l, r):
        """
        根据子串 s[l..r] 从状态 st 进行转移。
        返回新的状态。
        """
        while l < r:
            if st.pos == self.get_node(st.v).get_len(r):
                # 在节点上，尝试根据下一个字符转移
                char = self.s[l]
                if char not in self.get_node(st.v).next:
                    return State(-1, -1)
                
                next_v = self.get_node(st.v).next[char]
                st = State(next_v, 0)
                if st.v == -1:
                    return st
            else:
                # 在边上，检查字符是否匹配
                node = self.get_node(st.v)
                edge_char = self.s[node.l + st.pos]
                
                if edge_char != self.s[l]:
                    return State(-1, -1)
                
                remaining_len_on_edge = node.get_len(r) - st.pos
                if r - l < remaining_len_on_edge:
                    # 子串比剩余边短，停在边上
                    return State(st.v, st.pos + (r - l))
                
                # 子串比剩余边长，消耗掉整个边并继续
                l += remaining_len_on_edge
                st.pos += remaining_len_on_edge

        return st

    def _split(self, st, r):
        """
        如果活动点在边上，则分裂该边，创建新的内部节点。
        返回新节点的索引。
        """
        node = self.get_node(st.v)
        if st.pos == node.get_len(r):
            # 活动点在节点上，无需分裂
            return st.v
        
        if st.pos == 0:
            # 活动点是父节点，返回父节点即可
            return node.par
        
        # 分裂边
        new_node_index = self.sz
        self.tree.append(Node(node.l, node.l + st.pos, node.par))
        self.sz += 1
        
        parent_node = self.get_node(node.par)
        char_on_edge = self.s[node.l]
        parent_node.next[char_on_edge] = new_node_index
        
        self.get_node(new_node_index).next[self.s[node.l + st.pos]] = st.v
        node.par = new_node_index
        node.l += st.pos

        return new_node_index

    def _get_link(self, v, r):
        """
        递归地计算并返回一个节点的后缀链接。
        使用 memoization 优化。
        """
        node = self.get_node(v)
        if node.link != -1:
            return node.link
        
        if node.par == -1:
            return 0
        
        parent_link = self._get_link(node.par, r)
        
        # 转移以找到后缀链接
        start_char_index = node.l + (node.par == 0)
        end_char_index = node.r
        to_state = self._go(State(parent_link, self.get_node(parent_link).get_len(r)), start_char_index, end_char_index)
        
        # 如果需要，分裂边以创建链接的目标节点
        return_node_index = self._split(to_state, r)
        node.link = return_node_index
        return return_node_index

    def _tree_extend(self, pos):
        """
        向树中添加一个新字符 s[pos]。
        """
        # 调整叶子节点的右边界 (Rule 1)
        # 这段代码里没有显式写，但其逻辑隐含在go和split中

        while True:
            # Rule 2: 沿着 ptr 路径，尝试添加新字符
            next_ptr = self._go(self.ptr, pos, pos + 1)
            
            if next_ptr.v != -1:
                # show-stopper 规则：新字符已存在，算法停止
                self.ptr = next_ptr
                return

            # Rule 3: 创建新叶子
            mid = self._split(self.ptr, pos)
            leaf_index = self.sz
            self.tree.append(Node(pos, self.n, mid))
            self.sz += 1
            self.get_node(mid).next[self.s[pos]] = leaf_index
            
            # 更新后缀链接
            old_ptr_v = self.ptr.v
            self.ptr.v = self._get_link(mid, pos)
            
            # 这里的pos代表当前扩展的字符串长度
            node_at_link = self.get_node(self.ptr.v)
            self.ptr.pos = node_at_link.r - node_at_link.l
            
            if not mid:
                # 如果分裂出的是根节点，则跳出循环
                break
            
    def build_tree(self):
        """
        构建后缀树的主函数。
        """
        # 为了保证所有后缀都以不同字符结尾，我们在字符串末尾添加一个特殊字符
        self.s += '$'
        self.n += 1
        
        for i in range(self.n):
            self._tree_extend(i)

# 使用示例
if __name__ == "__main__":
    s = "cabab"
    st = SuffixTree(s)
    st.build_tree()
    
    # 打印树的结构以验证
    print("节点总数:", st.sz)
    for i in range(st.sz):
        node = st.tree[i]
        substring = st.s[node.l : node.r]
        print(f"节点 {i}: 边 {substring}, 父节点 {node.par}, 后缀链接 {node.link}")
        print(f"    子节点: {node.next}")