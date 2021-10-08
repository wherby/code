class Solution(object):
    def braceExpansionII(self, expression):
        n= len(expression)

        def product(a,b):
            #print("a:",a)
            #print("b:",b)
            #print(a,b)
            res =[]
            for x in a:
                for y in b:
                    res.append(x+y)
            if len(a) == 0 or len(b) ==0:
                res = a +b
            #print(res , "product by " ,a,b)
            return list(set(res))
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
        def dfs(start,end):
            #print(start,end)
            stack = []
            cur = []
            i= start
            while i<= end:
                t = expression[i]
                if t == "{":
                    j = i+1
                    k= findPair(expression,j)
                    next = dfs(i+1,k-1)
                    #print("1",cur,next)
                    cur  = product(cur,next)
                    i = k
                elif t == ",":
                    #print("cccc")
                    stack.append(cur)
                    cur = []
                else:
                    j = i+1
                    while j <= end and expression[j].isalpha():
                        j+=1
                    next = [expression[i:j]]
                    #print("2",cur,next,expression,i,j)
                    cur = product(cur,next)
                    i = j-1
                i +=1
                
            while len(stack )>0:
                for x in stack[-1]:
                    cur.append(x)
                stack.pop()
            #print("start, end ", start,end, cur,stack)
            return cur
        re =dfs(0,n-1)
        return sorted(list(set(re)))


re = Solution().braceExpansionII("{a,b},x{c,{d,e}y}")
print(re)
