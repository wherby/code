from collections import defaultdict
class Solution(object):
    def distinctNames(self, ideas):
        """
        :type ideas: List[str]
        :rtype: int
        """
        dic = defaultdict(set)
        for idea in ideas:
            dic[idea[0]].add(idea[1:])
        
        #print(dic)
        sm =0
        chars = 'abcdefghijklmnopqrstuvwxyz'
        for c1 in chars:
            s1 =dic[c1]
            for c2 in chars:
                s2 = dic[c2]
                k =len(s1 & s2)
                sm += (len(s1) -k)*(len(s2)-k)
                #print(sm)
                #print(k,s1,s2,c2,c1)
        return sm
    
re =Solution().distinctNames(ideas =["aaa","baa","caa","bbb","cbb","dbb"])
print(re)