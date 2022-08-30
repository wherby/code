# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution(object):
    def amountOfTime(self, root, start):
        """
        :type root: Optional[TreeNode]
        :type start: int
        :rtype: int
        """
        dic=defaultdict(list)
        def dfs(node):
            if node == None :
                return
            if node.left !=None:
                dic[node.val].append(node.left.val)
                dic[node.left.val].append(node.val)
                dfs(node.left)
            if node.right != None:
                dic[node.val].append(node.right.val)
                dic[node.right.val].append(node.val)
                dfs(node.right)
        dfs(root)
        visit={}
        visit[start]=1
        q =[start]
        cnt =-1
        while len(q)>0:
            tmp = []
            for b in q:
                for a in dic[b]:
                    if a not in visit:
                        tmp.append(a)
                        visit[a] =1
            cnt +=1
            q = tmp
        return cnt


re =Solution()
print(re)