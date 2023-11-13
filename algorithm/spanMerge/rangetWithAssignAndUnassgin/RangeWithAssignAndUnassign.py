# https://leetcode.cn/problems/range-module/solutions/1613356/shua-ti-ka-pei-guan-by-coding-cafe-flf3/?envType=daily-question&envId=2023-11-12
#https://leetcode.cn/problems/range-module/description/?envType=daily-question&envId=2023-11-12
class TreeNode:
    def __init__(self, l, r, v):
        self.left = l
        self.right = r 
        self.val = v

class ChthollyTree:
    def __init__(self, ):
        self.nodes = []

    def bsearch(self, pos):
        n = len(self.nodes)
        left, right = 0, n-1
        while left <= right: 
            mid = (right - left)//2 + left 
            if self.nodes[mid].left < pos:
                left = mid + 1 
            elif self.nodes[mid].left > pos:
                right = mid - 1 
            else: 
                return mid, False 
        return left, True 

    def split(self, pos):
        left, flag = self.bsearch(pos)
        if not flag: 
            return left
        left -= 1 
        l, r, v = self.nodes[left].left, self.nodes[left].right, self.nodes[left].val 
        del self.nodes[left]
        tr = TreeNode(l, pos-1, v)  
        self.nodes.insert(left, tr)
        tr = TreeNode(pos, r, v)
        self.nodes.insert(left+1, tr)
        return left+1

    def assign(self, l, r, v): 
        if len(self.nodes) == 0: 
            tr = TreeNode(l, r, v) 
            self.nodes.append(tr)
            return 
        itr = self.split(r+1)
        itl = self.split(l) 
        del self.nodes[itl:itr]
        tr = TreeNode(l, r, v) 
        self.nodes.insert(itl, tr) 

class RangeModule:

    def __init__(self):
        self.ct = ChthollyTree() 
        self.ct.assign(1, 1e9, 0) 

    def addRange(self, left: int, right: int) -> None:
        itr = self.ct.split(right)
        itl = self.ct.split(left)
        self.ct.assign(left, right-1, 1) 

    def queryRange(self, left: int, right: int) -> bool:
        right -= 1 
        itr, _ = self.ct.bsearch(right) 
        if itr >= len(self.ct.nodes): 
            return False 
        if self.ct.nodes[itr].left > right: 
            itr = max(itr-1, 0)  
        itl, _ = self.ct.bsearch(left) 
        if self.ct.nodes[itl].left > left: 
            itl = max(itl-1, 0)    
        if self.ct.nodes[itl].left > left or self.ct.nodes[itr].right < right: 
            return False
        for i in range(itl, itr+1): 
            if self.ct.nodes[i].val == 0: 
                return False 
            if i != itl and self.ct.nodes[i].left-1 > self.ct.nodes[i-1].right: 
                return False 
        return True 

    def removeRange(self, left: int, right: int) -> None:
        itr = self.ct.split(right)
        itl = self.ct.split(left)
        self.ct.assign(left, right-1, 0) 

#作者：Sholmes
#链接：https://leetcode.cn/problems/range-module/solutions/1613356/shua-ti-ka-pei-guan-by-coding-cafe-flf3/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。