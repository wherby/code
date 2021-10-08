class Solution(object):
    def braceExpansionII(self, expression):
        s =""
        for e in expression:
            if e.isalpha():
                s += "{"
                s += e
                s +="}"
            else:
                s += e
        stackStr =[-1]
        stackOp =[-1]
        curr =[]

        def evalStack(curr):
            while stackOp[-1] ==1:
                curr = combine(stackStr[-1],curr)
                #print("after combine:", curr)
                stackStr.pop()
                stackOp.pop()
            if stackOp[-1] == 0:
                curr = crossProduct(stackStr[-1],curr)
                #print("after cross:",curr)
                stackOp.pop()
                stackStr.pop()
            return curr
        def combine(a,b):
            #print("a,b combined by:",a,b )
            return list(set(a+b))

        def crossProduct(a,b):
            res =[]
            for x in a:
                for y in b:
                    res.append(x+y)
            if len(a) == 0 or len(b) ==0:
                res = a +b
            #print(res , "product by " ,a,b)
            return list(set(res))

        for e in s:
            #print(stackStr,stackOp)
            if e == "{":
                stackStr.append(list(curr))
                stackOp.append(0)
                #print(stackStr)
                curr =[]
            elif e == ",":
                stackStr.append(list(curr))
                stackOp.append(1)
                curr =[]
            elif e == "}":
                curr = evalStack(curr)
            else:
                curr.append(e)
                #print(curr,e)
        while stackOp[-1] != -1:
            curr= evalStack(curr)
        #print(stackStr,stackOp)
        return sorted(curr)
        



#re = Solution().braceExpansionII("{a,b}{c,{d,e}}")
re = Solution().braceExpansionII("{a,b},x{c,{d,e}y}")
print(re)
