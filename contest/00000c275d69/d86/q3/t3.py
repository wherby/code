def allState(k,m):
    ret=[]
    state = (1<<k) -1
    while (state <(1<<m)):
        ret.append(state)
        c = state &(-state)
        r = state +c
        state= (((r ^ state) >>2)//c) |r 
    return ret
class Solution(object):
    def maximumRows(self, mat, cols):
        """
        :type mat: List[List[int]]
        :type cols: int
        :rtype: int
        """
        m,n = len(mat),len(mat[0])
        
        def count(cols,state):
            tls =[[] for _ in range(m)]
            for j in range(n):
                if (1<<j) &state ==0:
                    for i in range(m):
                        tls[i].append(mat[i][j]) 
            cnt =0 
            for i in range(m):
                isG = True
                for a in tls[i]:
                    if a ==1:
                        isG = False
                if isG:cnt +=1
            return cnt
        state = allState(cols,n)
        mx = 0 
        for a in state:
            mx = max(mx,count(cols,a))
        return mx

re =Solution().maximumRows(mat = [[0,0,1],[1,0,0],[0,0,0]], cols = 2)
print(re)