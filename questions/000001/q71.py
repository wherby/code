
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        st =[]
        status =0
        tp =""
        path = path+"/"
        for a in path:
            if status ==0 and a =="/":
                if len(tp)>0:
                    st.append(tp)
                tp = ""
            elif a =="." and status ==0 and len(tp) ==0:
                tp += "."
                status =1
            elif a =="." and status ==1:
                tp +="."
                status =2
            elif a =="." and status ==2:
                status =0
                tp += "."
            elif a =="/" and status ==1:
                status=0
                tp=""
            elif a =="/" and status ==2:
                status =0
                if len(st)>0:
                    st.pop()
                tp=""
            else:
                tp +=a
                status =0
            #print(a,status,st,tp)
        res ="/" + "/".join(st)
        #print(res)
        return res


# re = Solution().simplifyPath(path = "/home/")
# re = Solution().simplifyPath(path = "/home//foo/")
# re = Solution().simplifyPath(path = "/a/./b/../../c/")
# re = Solution().simplifyPath("/../")
#re = Solution().simplifyPath("/a//b////c/d//././/..")
re = Solution().simplifyPath("/../")
print(re)
