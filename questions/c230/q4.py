class Solution(object):
    def getCollisionTimes(self, cars):
        n = len(cars)
        ret = [-1]*n

        st =[]
        st.append((0,cars[-1][1]))
        
        for i in range(n-2,-1,-1):
            ds=cars[i+1][0]-cars[i][0]
            vv = cars[i][1]
            total = 0

            if vv <= st[0][1]:
                st =[]
                st.append((0,vv))
                #print("CC")
                continue
            
            t = st[-1][0]
            v = st[-1][1]
            st.pop()
            while st:
                if total + v*(st[-1][0] -t) + ds >= vv* st[-1][0]:
                    total += v *(st[-1][0] -t)
                    t = st[-1][0]
                    v=st[-1][1]
                    st.pop()
                else:
                    break
            
            dt = (ds - (t * vv -total)) *1.0 / (vv-v)
            st.append((t+dt,v))
            st.append((0,vv))
            #print("cc",i)
            ret[i] = t +dt
        return ret

re = Solution().getCollisionTimes(cars = [[3,4],[5,4],[6,3],[9,1]])
print(re)
