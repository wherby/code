#https://leetcode.cn/problems/Jf1JuT/solution/wai-xing-wen-zi-dian-by-leetcode-solutio-to66/
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        inD ={}
        for w1 in words:
            for a in w1:
                inD[a] =0
        g = defaultdict(list)
        for s,t in pairwise(words):
            for u,v in zip(s,t):
                if u != v:
                    g[u].append(v)
                    inD[v] +=1
                    break
            else:                   ##  break operation  in for will change else condition
                if len(s)> len(t):
                    return ""
        q = [u for u,d in inD.items() if d ==0]
        for u in q :
            for v in g[u]:
                inD[v] -=1
                if inD[v] ==0:
                    q.append(v)
        return ''.join(q) if len(q) == len(inD) else ""