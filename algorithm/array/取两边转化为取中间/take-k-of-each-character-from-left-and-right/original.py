# https://leetcode.cn/problems/take-k-of-each-character-from-left-and-right/?envType=daily-question&envId=2024-09-27

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        pre=[[0]*3]
        pos =[[0]*3]
        for i in range(n):
            p1,p2 =list(pre[-1]),list(pos[-1])
            p1[ord(s[i]) - ord('a')] +=1
            p2[ord(s[-(i+1)]) -ord('a')]+=1
            pre.append(p1)
            pos.append(p2)
        lcur = n
        ret = n
        if pre[-1][0]<k or pre[-1][1]<k or pre[-1][2]<k:
            return -1 
        for i in range(n+1):
            acc =list(pre[i])
            lcur = min(lcur, n -i)
            while lcur >=0 and acc[0]+pos[lcur][0]>=k and acc[1]+pos[lcur][1]>=k and acc[2]+ pos[lcur][2]>=k:
                lcur -=1
            ret = min(ret,i+lcur+1)
        return ret