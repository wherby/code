import heapq
class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        st =[[a,"a"],[b,"b"],[c,"c"]]
        st.sort()
        re =""
        lastC="z"
        lastC2="z2"
        while st[2][0] !=0:
            if len(re)>=2:
                lastC =re[-2]
                lastC2=re[-1]
            fd =False
            for i in range(2,-1,-1):
                if st[i][0]>0 and (st[i][1] != lastC or lastC !=lastC2):
                    fd =True
                    re += st[i][1]
                    st[i][0] -=1
                    break
            if fd ==False:
                break
            st.sort()
        return re

re =Solution().longestDiverseString(a = 1, b = 1, c = 7)
print(re)

