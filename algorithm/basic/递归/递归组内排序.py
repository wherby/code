
# https://leetcode.cn/problems/special-binary-string/description/?envType=daily-question&envId=2026-02-20


class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        cnt = left = 0
        sub = list()

        for i,a in enumerate(s):
            if a =="1":
                cnt +=1
            else:
                cnt -=1 
                if cnt ==0:
                    sub.append("1" + self.makeLargestSpecial(s[left+1:i]) +"0")
                    left = i+1
        sub.sort(reverse= True)
        return "".join(sub)
                