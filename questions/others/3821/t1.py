#https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/610/week-3-july-15th-july-21st/3821/
class Solution(object):
    def verifySeed(self,ls,i,n):
        if ls[i] =='L' and i >0 and ls[i-1] =='.':
            return True
        elif ls[i] =='R' and i < n-1 and ls[i+1] == '.':
            return True
        return False
    
    def move(self,ls, res):
        n = len(ls)
        ress =[]
        moveL=[]
        moveR =[]
        for i in res:
            if ls[i] == 'L' and i ==1 and ls[0]=='.':
                moveL.append(i-1)
            if ls[i] == 'L' and i >1 and ls[i-1] =='.' and ls[i-2] != 'R':
                moveL.append(i-1)
                ress.append(i-1)
            if ls[i] =="R" and i == n -2 and ls[i+1] =='.':
                moveR.append(i+1)
            if ls[i] =='R' and i < n-2 and ls[i+1] =='.' and ls[i+2] != 'L':
                moveR.append(i+1)
                ress.append(i+1)
        for i in moveL:
            ls[i]='L'
        for i in moveR:
            ls[i]='R'
        return ress 
 
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        ls = list(dominoes)
        n = len(ls)
        res = [i for i in range(n)  if self.verifySeed(ls,i,n)]
        while len(res)>0:
            res = self.move(ls,res)
        return "".join(ls)

a = Solution().pushDominoes(".L.R.")
print(a)