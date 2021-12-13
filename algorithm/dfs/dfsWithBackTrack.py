# https://leetcode-cn.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/submissions/
# Dirs 记录路径
# TDK dfs backtrack
def dfs(node, dirs,target):
    if node == None : return False
    if node.val ==target : return True

    if node.left:
        dirs.append("L")
        if dfs(node.left,dirs,target):
            return True
        dirs.pop()
    if node.right:
        dirs.append("R")
        if dfs(node.right,dirs,target):
            return True
        dirs.pop()
    return False