class Solution(object):
    def garbageCollection(self, garbage, travel):
        """
        :type garbage: List[str]
        :type travel: List[int]
        :rtype: int
        """
        ls= [0]*3
        acc =0
        for i,gs in enumerate(garbage):
            acc += len(gs)
            for a in gs:
                if a =="M":
                    ls[0]=i
                if a =="P":
                    ls[1]=i
                if a =="G":
                    ls[2]=i
        travel = [0]+ travel
        for i in range(3):
            acc += sum(travel[:ls[i]+1])
        return acc
            
        




re =Solution().garbageCollection(garbage = ["MMM","PGM","GP"], travel = [3,10])
print(re)