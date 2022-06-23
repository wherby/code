# 找到最左的点，然后找到一个点使得所有点都在这两点连线的一侧。
class Solution:
    def outerTrees(self, trees: list[list[int]]) -> list[list[int]]:
        def cross(p,q,r):
            return (q[0] - p[0])*(r[1]-q[1]) - (q[1]-p[1]) *(r[0]-q[0])
        n = len(trees)
        if n < 4:
            return trees
        
        leftMost =0
        for i,tree in enumerate(trees):
            if tree[0]< trees[leftMost][0]:
                leftMost =i
        
        ans = []
        vis = [0]*n
        p =leftMost
        while True:
            q = (p+1)%n
            for i,tree in enumerate(trees):
                #if vis[i]:continue
                #// 如果 r 在 pq 的右侧，则 q = r
                if cross(trees[p],trees[q],tree) <0:
                    q= i
            #  是否存在点 i, 使得 p q i 在同一条直线上 查找所有在边界上的点
            for i,b in enumerate(vis):
                if not b and i!=p and i !=q and cross(trees[p],trees[q],trees[i]) ==0:
                    ans.append(trees[i])
                    vis[i] =1
            if not vis[q]:
                ans.append(trees[q])
                vis[q] =1
            p = q
            #print(p,vis,leftMost)
            if p == leftMost:
                break
        return ans

t2 =[[3,3],[2,4],[2,2],[7,4],[3,4]]
t1 =[[3,0],[4,0],[5,0],[6,1],[7,2],[7,3],[7,4],[6,5],[5,5],[4,5],[3,5],[2,5],[1,4],[1,3],[1,2],[2,1],[4,2],[0,3]]            
re =Solution().outerTrees(t1)
print(re)