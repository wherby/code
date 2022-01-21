from collections import defaultdict
class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        visit = [0]*n
        st = [(n-1,0)]
        visit[n-1] =1
        dic = defaultdict(list)
        for i,a in enumerate(arr):
            dic[a].append(i)
        while st:
            idx,c =st.pop(0)
            if idx ==0:
                return c
            for a in dic[arr[idx]]:
                if visit[a] ==0:
                    visit[a] =1
                    st.append((a,c+1))
            del dic[arr[idx]]
            if idx < n-1 and visit[idx +1] ==0:
                visit[idx+1] =1
                st.append((idx+1,c+1))
            if idx >0 and visit[idx-1] ==0:
                visit[idx-1] =1
                st.append((idx-1,c+1))
            
