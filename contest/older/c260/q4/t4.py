class Solution(object):
    
    def scoreOfStudents(self, s, answers):
        """
        :type s: str
        :type answers: List[int]
        :rtype: int
        """
        n = len(s)
        nums = []
        op=[]
        for i in range(n):
            if i%2 ==1:
                op.append(s[i])
            else:
                nums.append(int(s[i]))
        print(nums)
        m = len(op)
        s1=""
        for i in range(m):
            if op[i] == "*":
                s1 =s1 +"1"
            else:
                s1=s1 +"0"

        def val(s1,nums,op):
            def doOp(t1,t2,op):
                if op == "+":
                    return t1 + t2
                else:
                    return t1 *t2
            m = len(s1)
            res = [nums[0]]
            print(nums)
            for i in range(m):
                t2 = nums[i+1]
                if s1[i] == "1":
                    t = res.pop()
                    t3 = doOp(t,t2,op[i])
                    res.append(t3)
                else:
                    res.append(t2)
            for i in range(m):
                if s1[m-1-i] =="0":
                    t1 = res.pop()
                    t2 = res.pop()
                    t3 = doOp(t1,t2,op[m-i -1])
                    res.append(t3)
            return res[0]
        res = val(s1,nums,op)
        ret = 0
        if res in answers:
            ret += 5
        for i in range(1 <<m):
            s =["0" ]* m
            t =i 
            index =0
            while t !=0:
                x = t%2
                if x == 1:
                    s[index] ="1"
                t = t/2
                index +=1
            s1 = "".join(s)
            res = val(s1,nums,op)
            if res in answers:
                ret +=2
        return ret

s = "7+3*1*2"
answers = [20,13,42]
re = Solution().scoreOfStudents(s,answers)
print(re)