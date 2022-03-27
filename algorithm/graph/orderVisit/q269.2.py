#https://leetcode-cn.com/problems/Jf1JuT/
from collections import deque
from collections import defaultdict

def orderVisit(inD,graph):
    st= deque([])
    res =[]
    for k,_ in graph.items():
        if inD[k] ==0:
            st.append(k)
    while st:
        t = st.popleft()
        res.append(t)
        for a in graph[t]:
            inD[a] -=1
            if inD[a] ==0:
                st.append(a)
    return res
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        inD = defaultdict(int)
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
                        inD[c2] +=1
                    break
        res = orderVisit(inD,graph)
        return "".join(res) if len(graph) == len(res) else ""


re = Solution().alienOrder(["wrt","wrf","er","ett","rftt"])
print(re)