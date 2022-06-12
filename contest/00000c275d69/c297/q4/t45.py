from collections import defaultdict
class Solution(object):
    def distinctNames(self, ideas):
        """
        :type ideas: List[str]
        :rtype: int
        """
        dic = defaultdict(set)
        for idea in ideas:
            dic[idea[1:]].add(idea[0])
        
        cs = 'abcdefghijklmnopqrstuvwxyz'
        cts = {a:{b:0 for b in cs} for a in cs}
        sm =0
        for key in dic:
            values = dic[key]
            
        return sm*2
    
    
re =Solution().distinctNames(["aaa","baa","caa","bbb","cbb","dbb"])
print(re)
