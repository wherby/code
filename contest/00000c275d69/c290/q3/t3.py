from bisect import bisect_left
class Solution(object):
    def countRectangles(self, rectangles, points):
        """
        :type rectangles: List[List[int]]
        :type points: List[List[int]]
        :rtype: List[int]
        """
        lls = [[] for _ in range(102)]
        for x,y in rectangles:
            lls[y].append(x)
        for i in range(102):
            lls[i].sort()
        n = len(points)
        ret = [0]*n
        for i,(x,y) in enumerate(points):
            cnt =0
            for j in range(y,101):
                if len(lls[j])>0:
                    k = bisect_left(lls[j],x)
                    cnt +=max(len(lls[j])-k,0)
            ret[i] = cnt
        return ret
    
re = Solution().countRectangles([[81,69],[85,18],[4,89],[2,23],[29,25],[19,98],[77,74],[100,98],[61,5],[11,57],[23,4],[2,55],[8,77],[23,79],[4,69],[4,33],[44,69],[93,47],[77,4],[44,91],[11,54],[35,67],[59,90],[34,59],[16,25],[93,6],[37,14],[88,51],[13,69],[16,26],[77,7],[6,63],[3,41],[90,89],[97,35],[75,49],[96,94],[80,16],[96,59]],[[26,16],[58,70],[64,58],[52,2],[85,98],[75,93],[12,3],[2,25],[79,90],[36,35],[45,40],[12,34],[2,71],[63,88],[74,91],[78,90],[73,19],[95,92],[43,7],[9,28]])
print(re)
                
        
        