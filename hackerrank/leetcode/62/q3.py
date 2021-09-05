#https://leetcode.com/contest/weekly-contest-by-app-academy/problems/closest-leaf-in-a-binary-tree/
#Diction record both children and parent of node.
#use dict.pop() will calc the distance from up and down two direction.
#
#
class Solution(object):
    def findClosestLeaf(self, root, k):
        # Time: O(n)
        # Space: O(n)
        from collections import defaultdict
        graph, leaves = defaultdict(list), set()
        # Graph construction
        def traverse(node):
            if not node:
                return
            if not node.left and not node.right:
                leaves.add(node.val)
                return
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                traverse(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                traverse(node.right)
        traverse(root)
        # Graph traversal - BFS
        queue = [k]
        while len(queue):
            next_queue = []
            for node in queue:
                if node in leaves:
                    return node
                next_queue += graph.pop(node, [])
            queue = next_queue