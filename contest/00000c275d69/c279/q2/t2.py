
class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        re = []
        if num >0:
            s1 = str(num)
            s1 = list(map(lambda x: int(x),s1))
            s1 = sorted(s1)
            idx =0
            for i,a in enumerate(s1):
                if a != 0:
                    idx = i
                    break
            re.append(s1[idx])
            for i,a in enumerate(s1):
                if i != idx:
                    re.append(a)
        elif num<0:
            s1 = str(num)[1:]
            s1 = list(map(lambda x: int(x),s1))
            s1 = sorted(s1,reverse= True) 
            re.append("-")
            for a in s1:
                re.append(a)
        else:
            re.append(0)
        #print(re)
        re= list(map(lambda x:str(x),re))
        re ="".join(re)
        return int(re)

re = Solution().smallestNumber(63)
print(re)