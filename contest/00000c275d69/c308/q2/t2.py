class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        st=[]
        for a in s:
            if a=="*":
                if len(st)>0:
                    st.pop()
            else:
                st.append(a)
        return "".join(st)




re =Solution()
print(re)