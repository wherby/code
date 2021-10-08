class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """

        stack=[""]
        n = len(expression)
        ex = expression
        def findPair(str, start):
            m = len(str)
            cnt =1
            for i in range(start,m):
                t = str[i]
                if t == "{":
                    cnt +=1
                if t =="}":
                    cnt -=1
                if cnt == 0:
                    return i
            return -1
        def product(a,b):
            print("product: " , a, b )
            res =[]
            for x in a:
                for y in b:
                    res.append(x+y)
            return list(set(res))

        def eval(str):
            if len(str) ==0:
                return [""]
            m = len(str)
            firstLeft = str.find("{")
            if firstLeft != -1:
                rightPair = findPair(str, firstLeft+1)
                left = str[:firstLeft]
                mid = eval(str[firstLeft+1:rightPair])
                right = eval(str[rightPair+1:])
                return left + mid +right
                
            else:
                
                
                return [str]

        res=evalBracket(expression)
        print(res)
        #return sorted(list(set(res)))

            

        


re = Solution().braceExpansionII("{a,b}{c,{d,e}}")
print(re)
                