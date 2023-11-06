class Solution(object):
    def goodDaysToRobBank(self, security, time):
        """
        :type security: List[int]
        :type time: int
        :rtype: List[int]
        """
        length = len(security)
        verifyPre=[0]*length
        verifyPost =[0]*length
        st =[]
        for i,n in enumerate(security):
            if len(st) ==0:
                if len(st) ==time:
                    verifyPre[i] = 1
                st.append((i,n))
            else:
                while st and st[-1][1]<n:
                    st.pop()
                st.append((i,n))
            if len(st) >= time+1 and st[-(time+1)][0] == i-time:
                    verifyPre[i] = 1
                
            # if st and st[0][0] <= i-time:
            #         st.pop(0)
        st=[]
        for i in range(length-1,-1,-1):
            n = security[i]
            #print(i,n)
            if len(st) ==0:
                if len(st) ==time:
                    verifyPost[i] = 1
                st.append((i,n))
            else:
                while st and st[-1][1]<n:
                    st.pop()
                st.append((i,n))
            if  len(st)>= time+1 and st[-(time+1)][0] ==i +time:
                    verifyPost[i] = 1
            # if st and st[0][0] >= i + time:
            #         #print(st[0])
            #         st.pop(0)
            #print(st)
        res =[]
        for i in range(length):
            if verifyPost[i] and verifyPre[i]:
                res.append(i)
        #print(verifyPre)
        #print(verifyPost)
        return res
        print(verifyPre)
        print(verifyPost)

re =Solution().goodDaysToRobBank(security = [1,1,1,1,1], time = 0)
print(re)
            