#https://leetcode-cn.com/problems/tag-validator/
class Solution(object):
    def isValid(self, code):
        """
        :type code: str
        :rtype: bool
        """
        tags =[]
        i,n = 0,len(code)
        while i<n:
            if code[i] !="<":
                if not tags:
                    return False
                i +=1
                continue
            if i == n-1:
                return False
            if code[i+1] =="/":
                j = code.find('>',i)
                if j == -1:
                    return False
                tagName = code[i+2:j]
                #print(tagName,tags, not tags , tags[-1] != tagName)
                if  not tags or  tags[-1] != tagName:
                    return False
                tags.pop()
                i= j+1
                if not tags and i !=n:
                    return False
            elif code[i+1] =="!":
                if not tags:
                    return False
                cdata = code[i+2:i+9]
                if cdata != "[CDATA[":
                    return False
                j= code.find("]]>",i)
                if j ==-1:
                    return False
                i = j+1
            else:
                j = code.find(">",i)
                if j ==-1:
                    return False
                tagName = code[i+1:j]
                if not 1<=len(tagName) <= 9 or not all(ch.isupper() for ch in tagName):
                    return False
                tags.append(tagName)
                i= j+1
        return not tags
    
re =Solution().isValid("<A>  <B> </A>   </B>")
print(re)