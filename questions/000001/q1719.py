from collections import defaultdict
class Solution(object):
    def checkWays(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        dic = defaultdict(set)
        for x,y in pairs:
            dic[x].add(y)
            dic[y].add(x)
        k = len(dic)
        root = next((node for node , neighbors in dic.items() if len(neighbors) == k-1),-1)
        if root ==-1 :
            return 0
        ans = 1 
        for node,neighburs in dic.items():
            print(node,neighburs)
            if node == root:
                continue
            currDegree = len(neighburs)
            parent = -1
            parentDegree = 10000000000
            for neighbor in neighburs:
                if currDegree <= len(dic[neighbor]) < parentDegree:
                    parent = neighbor
                    parentDegree = len(dic[neighbor])
            if parent == -1 or any(neighbor != parent and neighbor not in dic[parent] for neighbor in neighburs):
                return 0
            if parentDegree == currDegree:
                ans =2
        return ans


re =Solution().checkWays(pairs = [[1,2],[2,3],[1,3]])
print(re)
        