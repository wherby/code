# https://www.youtube.com/watch?v=lbN7RBaSYb4&ab_channel=HuifengGuan  //TODO..
# https://leetcode-cn.com/problems/rank-transform-of-a-matrix/submissions/ Not work for the aggration all same value.. Not AC yet
from collections import defaultdict
from typing import Sized
class Solution:
    def matrixRankTransform(self, matrix: list[list[int]]) -> list[list[int]]:
        inDegree=defaultdict(int)
        children= defaultdict(list)
        m,n = len(matrix), len(matrix[0])
        res =[[0]*n for _ in range(m)]
        for i in range(m):
            lsT= matrix[i]
            lsT= list(set(lsT))
            lsT.sort()
            for t in range(len(lsT)):
                t1 = lsT[t]
                inDegree[t1] += t
                for j in range(t+1,len(lsT)):
                    children[t1].append(lsT[j])
        for j in range(n):
            lsT = []
            for i in range(m):
                lsT.append(matrix[i][j])
            #print(lsT)
            lsT= list(set(lsT))
            lsT.sort()
            for k in range(len(lsT)):
                t1 = lsT[k]
                inDegree[t1] += k
                for z in range(k+1,len(lsT)):
                    children[t1].append(lsT[z])
        #print(matrix)
        hp = []
        for k,v in inDegree.items():
            if v ==0:
                hp.append(k)
        idx = 1
        #print(inDegree)
        while hp:
            tmpHp=[]
            for t in hp:
                for i in range(m):
                    for j in range(n):
                        if matrix[i][j]  == t:
                            res[i][j] = idx
                for t2 in children[t]:
                    inDegree[t2] -=1
                    if inDegree[t2] ==0:
                        tmpHp.append(t2)
            hp =tmpHp
            idx +=1
        return res

re =Solution().matrixRankTransform(matrix = [[1,2],[3,4]])
print(re)
        
