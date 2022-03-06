from collections import defaultdict
class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        g={}
        dic={}
        for f,t,l in descriptions:
            g[f*2 +l] =t
            dic[t] =1
        root =-1
        for f,t,l in descriptions:
            if f not in dic:
                root =f
        head = TreeNode(root)
        st = [head]
        while st:
            cur = st.pop(0)
            k = cur.val
            if k*2+l in g:
                t = TreeNode(g[k*2+1])
                cur.left =t
                st.append(t)
            if k*2 in g:
                t = TreeNode(g[k*2])
                cur.right = t
                st.append(t)
        return head
