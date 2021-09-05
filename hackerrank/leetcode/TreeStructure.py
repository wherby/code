
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def readTree(inTree):
    n =len(inTree)
    root = TreeNode(inTree[0])
    queue =[root]
    for i in range(1,n,2):
        node= queue.pop(0)
        if inTree[i] != None:
            left = TreeNode(inTree[i])
            node.left=left
            queue.append(left)
        if inTree[i+1] !=None:
            right = TreeNode(inTree[i+1])
            node.right=right
            queue.append(right)
    return root


def printTree(root):
    def printNode(node):
        if node == None:
            #print "None"
            return ""
        print node.val
        printNode(node.left)
        printNode(node.right)
    printNode(root)










inTree= [10,5,15,None,None,6,20]
root= readTree(inTree)
printTree(root)