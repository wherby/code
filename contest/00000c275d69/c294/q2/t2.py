class Solution(object):
    def maximumBags(self, capacity, rocks, addi):
        """
        :type capacity: List[int]
        :type rocks: List[int]
        :type additionalRocks: int
        :rtype: int
        """
        n = len(capacity)
        cnt =0 
        ls =[]
        for i in range(n):
            if capacity[i]> rocks[i]:
                ls.append(capacity[i]-rocks[i])
            else:
                cnt +=1
        ls.sort()
        for a in ls:
            if a <= addi:
                addi -=a 
                cnt +=1
        return cnt