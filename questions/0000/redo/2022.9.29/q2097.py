from collections import defaultdict


class Solution(object):
    def validArrangement(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: List[List[int]]
        """
        def visit(start,g):
            st = [start]
            route=[]
            while st:
                while g[st[-1]]:
                    st.append(g[st[-1]].pop())   # 对于邻接点的选择可能有优先队列  #https://leetcode-cn.com/problems/reconstruct-itinerary/submissions/
                route.append(st.pop())
            route.reverse()
            return [[route[i], route[i+1]] for i in range(len(route)-1)]
        inD = defaultdict(int)
        g = defaultdict(list)
        for a,b in pairs:
            inD[a] +=1
            inD[b] -=1
            g[a].append(b)
        start = -1
        for a,b in pairs:
            if inD[a]%2 ==1 and inD[a] >0:
                start =a
                break
        if start ==-1:
            start = pairs[0][0]
        #print(start,inD)
        ls = visit(start,g)
        return ls

ls  = [[874,518],[649,247],[621,559],[774,166],[241,168],[835,421],[168,835],[835,399],[741,436],[958,526],[166,578],[734,812],[436,297],[813,774],[166,559],[518,548],[882,719],[559,741],[819,621],[720,168],[964,187],[518,781],[166,781],[781,436],[719,958],[342,241],[659,392],[27,513],[812,468],[513,910],[187,848],[510,741],[835,392],[813,559],[392,848],[964,813],[241,958],[958,436],[854,241],[813,719],[781,421],[421,649],[720,910],[510,297],[725,835],[848,271],[483,578],[848,336],[854,592],[559,720],[436,399],[297,958],[592,483],[526,734],[854,813],[40,720],[719,510],[548,964],[910,882],[342,854],[578,518],[399,514],[514,813],[22,854],[399,342],[336,297],[392,271],[813,835],[27,166],[436,725],[271,854],[468,659],[421,166],[168,548],[297,526],[271,964],[741,725],[548,27],[910,510],[559,27],[73,40],[526,510],[247,819],[725,874],[578,342],[297,22],[510,813]]
re = Solution().validArrangement(pairs = ls)
print(re)