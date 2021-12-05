# 单次LCA for tree https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/discuss/1612179/Python3-lca
class LCA:
    def getLCA(self,node,valueA,valueB):
        if not node:
            return
        if node.val in (valueA,valueB):
            return node
        left,right= self.getLCA(node.left,valueA,valueB),self.getLCA(node.right,valueA,valueB)
        if left and right:
            return node
        return left or right

    def traceA(self,node,value,record):
        if not node: return False
        if node.val == value:
            return True
        left,right = self.trace(node.left,value,record), self.trace(node.right,value,record)
        if left:
            record.append("L")
            return True
        if right:
            record.append("R")
            return True
        
        


