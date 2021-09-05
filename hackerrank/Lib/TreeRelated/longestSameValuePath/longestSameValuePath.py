
class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        self.ans = 0

        def arrow_length(node):
            if not node: return 0
            left_length = arrow_length(node.left)
            right_length = arrow_length(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1
            ## update gloable vaue in the child node counting 
            self.ans = max(self.ans, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        arrow_length(root)
        return self.ans


if __name__=="__main__":
    root = TreeNode(5)
    leftNode = TreeNode(5)
    rightNode = TreeNode(5)
    root.left = leftNode
    root.right = rightNode
    leftNode.left = TreeNode(5)
    leftNode.right = TreeNode(1)
    rightNode.right = TreeNode(5)
    s = Solution()
    print s.longestUnivaluePath(root)