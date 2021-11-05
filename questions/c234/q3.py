class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        dic = {}
        for k in knowledge:
            dic[k[0]] = k[1]
        res =""
        t = ""
        state =0
        for a in s:
            if a =="(":
                state =1
                continue
            elif a ==")":
                state =0
                if t in dic:
                    res += dic[t]
                else:
                    res += "?"
                t=""
            elif state ==1:
                t +=a
            else:
                res +=a
        return res




s = "(name)is(age)yearsold"
knowledge = [["name","bob"],["age","two"]]
re = Solution().evaluate(s,knowledge)
print(re)