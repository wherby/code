#https://leetcode-cn.com/problems/Jf1JuT/

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        inD = [0]*26
        graph={}
        for word in words:
            for a in word:
                graph[a] =set()
        n = len(words)
        def precheck(w1,w2):
            if w1.find(w2)==0 and  len(w1)>len(w2):
                return True
            return False
        for i in range(1,n):
            w1 =words[i-1]
            w2 =words[i]
            if precheck(w1,w2):return ""
            for j in range(min(len(w1),len(w2))):
                c1,c2= w1[j],w2[j]
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        inD[ord(c2)-ord('a')] +=1
                    break
        q =[]
        for k,v in graph.items():
            if inD[ord(k)-ord('a')] == 0:
                q.append(k)
        res=""
        while q:
            t= q.pop(0)
            res+=t
            for a in graph[t]:
                inD[ord(a)-ord('a')] -=1
                if inD[ord(a)-ord('a')] ==0:
                    q.append(a)
        return res if len(graph) == len(res) else ""
        



re = Solution().alienOrder(["wrt","wrf","er","ett","rftt"])
print(re)