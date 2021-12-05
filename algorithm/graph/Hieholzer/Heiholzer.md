
# 会有 “maximum recursion depth exceeded while calling a Python object” 递归层数问题 和超时

        def dfs(start,res):
            if len(dic2[start]) ==0:
                return
            k =dic2[start].pop()
            tmp=[]
            tmp.append([start,k])
            dfs(k,tmp)   
            while len(dic2[start]):
                k = dic2[start].pop()
                anotherCircle = [[start,k]]
                anotherCircle=dfs(k,anotherCircle)
                res.extend(anotherCircle)
            res.extend(tmp)
            return res

用stack 解决递归和合并问题

def visit(start,g):
    st = [start]
    route=[]
    while st:
        while g[st[-1]]:
            st.append(g[st[-1]].pop())
        route.append(st.pop())
    route.reverse()
    return [[route[i], route[i+1]] for i in range(len(route)-1)]