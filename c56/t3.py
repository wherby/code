class Solution(object):
    def sumSub(self,num,start,end):
        res =0
        for i in range(start,end):
            if num[i] !="?":
                res = res + int(num[i])
        return res
    
    def questNum(self,num,start,end):
        res =0
        for i in range(start,end):
            if num[i] =="?":
                res = res + 1
        return res

    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        qusNum =0
        m = len(num)
        n = m//2
        for i in num:
            if i == "?":
                qusNum = qusNum +1
        if qusNum ==0:
            if self.sumSub(num,0,n) == self.sumSub(num,n,m):
                return False
            else:
                return True
        left = self.sumSub(num,0,n)
        right = self.sumSub(num,n,m)
        leftQ = self.questNum(num,0,n)
        rightQ = self.questNum(num,n,m)
        allQ = self.questNum(num,0,m)
        if allQ %2 == 1:
            return True
        if left> right:
            dif = left -right
            if leftQ >= rightQ:
                return True
            if dif == (rightQ -leftQ) /2 *9:
                return False
            else:
                return True
        elif left< right:
            dif = right -left
            if rightQ >= leftQ:
                return True
            if dif == ( leftQ -rightQ)/2 *9:
                return False
            else:
                return True
        else:
            if rightQ ==leftQ:
                return False
            else:
                return True


a = Solution().sumGame("?3295???")
print(a)
            