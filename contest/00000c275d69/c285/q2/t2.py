class Solution(object):
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """
        st =[]
        cnt =0
        for a in directions:
            if a =="L" and len(st)==0:
                continue
            if a =="L" :
                if st[-1]=="R":
                    st.pop()
                    cnt +=2
                else:
                    st.pop()
                    cnt +=1
                while st and st[-1]=="R":
                    st.pop()
                    cnt +=1
                st.append("S")
            elif a =="R" :
                st.append(a)
            else:
                while st and st[-1] =="R":
                    st.pop()
                    cnt +=1
                st.append(a)
            #print(a,st,cnt)
        return cnt

re = Solution().countCollisions("SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR")
print(re)

            