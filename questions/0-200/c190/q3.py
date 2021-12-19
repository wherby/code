from collections import defaultdict
class Solution(object):
    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        cnt = 0
        dic =defaultdict(int)
        def check():
            odd = 0
            for k,v in dic.items():
                if v %2 ==1:
                    odd +=1
            return odd <=1 
        def dfs(root):
            nonlocal cnt
            if root == None:
                return
            dic[root.val] +=1
            if root.left == None and root.right ==None:
                if check():
                    cnt +=1
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            dic[root.val] -=1
        dfs(root)
        return cnt


            