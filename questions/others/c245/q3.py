from collections import defaultdict
class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        n = len(triplets)
        ls= [0]*n
        dic = defaultdict(list)
        for i in range(n):
            t = triplets[i]
            tp= 0
            for j in range(3):
               # print(t[j],target[j])
                if t[j] == target[j]:
                    tp =tp + (1<<j)
                elif t[j]> target[j]:
                    tp=-1
                    break
            if tp >0:
                dic[tp].append(i)
        #print(dic)
        keys = dic.keys()
        re =0
        for k in keys:
            re = re |k
        return re == 7


re = Solution().mergeTriplets(triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5])
print(re)
            
