from bisect import bisect_left
class Solution(object):
    def minOperations(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: int
        """
        dic ={}
        for i in range(len(target)):
            dic[target[i]] =i
        ls =[]
        for a in arr:
            if a in dic:
                ls.append(dic[a])
        n = len(ls)
        sk =[]
        for x in ls:
            if len(sk) == 0 or x > sk[-1]:
                sk.append(x)
            else:
                idx = bisect_left(sk,x)
                sk[idx] = x
            

        return len(target) - len(sk)
        



re =Solution().minOperations(target = [17,18,14,13,6,9,1,3,2,20], arr = [18,15,14,6,6,13,15,20,2,6])
print(re)