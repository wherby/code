#https://leetcode.cn/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/

# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution(object):
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        if quadTree1.isLeaf:
            return Node(True,True) if quadTree1.val else quadTree2
        if quadTree2.isLeaf:
            return self.intersect(quadTree2,quadTree1)
        a1 = self.intersect(quadTree1.topLeft,quadTree2.topLeft)
        a2 = self.intersect(quadTree1.topRight,quadTree2.topRight)
        a3 = self.intersect(quadTree1.bottomLeft,quadTree2.bottomLeft)
        a4 = self.intersect(quadTree1.bottomRight,quadTree2.bottomRight)
        if a1.isLeaf and a2.isLeaf and a3.isLeaf and a4.isLeaf and a1.val ==a2.val == a3.val ==a4.val:
            return Node(a1.val,True)
        return Node(False,False,a1,a2,a3,a4)