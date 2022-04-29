from functools import cmp_to_key
# 先选bottom点，然后用极坐标排序，如果出现cross <0说明出现内凹，则把点移除

class Solution:
    def outerTrees(self, trees: list[list[int]]) -> list[list[int]]:
        def cross(p,q,r):
            return (q[0] - p[0])*(r[1]-q[1]) - (q[1]-p[1]) *(r[0]-q[0])
        def distance(p,q):
            return (p[0]-q[0])*(p[0]-q[0])+(p[1]-q[1])*(p[1]-q[1])
        n = len(trees)
        if n < 4:
            return trees
        bottom = 0
        for i, tree in enumerate(trees):
            if tree[1] < trees[bottom][1]:
                bottom =i
        trees[bottom], trees[0] = trees[0], trees[bottom]
        # 以 bottom 原点，按照极坐标的角度大小进行排序
        def cmp(a,b):
            diff =cross(trees[0],b,a) -cross(trees[0],a,b)
            return diff if diff else distance(trees[0],a) - distance(trees[0],b)
        trees[1:] = sorted(trees[1:],key = cmp_to_key(cmp))
        
        # 对于凸包最后且在同一条直线的元素按照距离从小到大进行排序
        r = n-1
        while r>0 and cross(trees[0],trees[n-1],trees[r]) ==0:
            r -=1
        l,h = r+1,n-1
        while l <h:
            trees[l],trees[h] = trees[h],trees[l]
            l +=1
            h -=1
        stack = [0,1]
        for i in range(2,n):
            while len(stack) >1 and cross(trees[stack[-2]],trees[stack[-1]],trees[i])<0:
                stack.pop()
            stack.append(i)
        return [trees[i] for i in stack]


t2 =[[3,3],[2,4],[2,2],[7,4],[3,4]]
t1 =[[3,0],[4,0],[5,0],[6,1],[7,2],[7,3],[7,4],[6,5],[5,5],[4,5],[3,5],[2,5],[1,4],[1,3],[1,2],[2,1],[4,2],[0,3]]            
re =Solution().outerTrees(t1)
print(re)