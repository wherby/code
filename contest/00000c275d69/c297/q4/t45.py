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
            for a in values:
                for b in cs:
                    if b in values: continue
                    sm += cts[a][b]
            for a in values:
                for b in cs:
                    if b in values: continue
                    cts[b][a] +=1
            
        return sm*2
    
    
re =Solution().distinctNames(["aaa","baa","caa","bbb","cbb","dbb"])
print(re)
