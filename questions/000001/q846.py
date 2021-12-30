from collections import defaultdict
class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        n = len(hand)
        if n%groupSize !=0:
            return False
        dic = defaultdict(int)
        for h in hand:
            dic[h] +=1
        cnt =0
        while cnt < n//groupSize:
            mn = min(dic.keys())
            for i in range(groupSize):
                t = mn +i
                if dic[t] <=0:
                    return False
                else:
                    dic[t] -=1
                    if dic[t] ==0:
                        del dic[t]
            cnt +=1
        return True

re = Solution().isNStraightHand(hand =[2,1], groupSize = 2)
print(re)