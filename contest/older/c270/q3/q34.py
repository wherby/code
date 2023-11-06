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

    def trace(self,node,value,record):
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
            

class Solution(object):
    
    def getDirections(self, root, startValue, destValue):
        lca = LCA()
        ancestor = lca.getLCA(root,startValue,destValue)
        sp,dp =[],[]
        lca.trace(ancestor,startValue,sp),lca.trace(ancestor,destValue,dp)
        while sp and dp and sp[-1] ==dp[-1]:
            sp.pop()
            dp.pop()
        return "".join(["U"]*len(sp)+dp[::-1])

