# find-duplicate-subtrees


##

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        dic ={}
        acc =0
        seen=set()
        def dfs(node):
            nonlocal acc
            if node ==None:
                return 0 
            hv = str(node.val) + "*"+ str(dfs(node.left)) + "*" + str(dfs(node.right))
            if hv not in dic:
                acc +=1
                dic[hv] = (acc,node) 
                return acc 
            else:
                idx,node = dic[hv]
                seen.add(node)
                return idx
        dfs(root)
        return list(seen)
    
## Wrong solution

## For nodes with same structure, and the hash value could be different
class Solution:
    def findDuplicateSubtrees(self, root) :
        dic ={}
        acc =0
        seen=set()
        def dfs(node):
            nonlocal acc
            if node ==None:
                return 0 
            hv = str(node.val) + "*"+ str(dfs(node.left)) + "*" + str(dfs(node.right))
            if hv not in dic:
                acc +=1
                dic[hv] = (acc,node) 
                return acc 
            else:
                idx,node2 = dic[hv]
                seen.add(node) ## This will add  dupilicated same structure nodes
                return idx
        dfs(root)
        return list(seen)
    