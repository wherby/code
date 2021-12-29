class Solution(object):
    def minimumOperations(self, nums, start, goal):
        """
        :type nums: List[int]
        :type start: int
        :type goal: int
        :rtype: int
        """
        visited =[0]*1001
        find = False
        mn =1000000
        st =[(start,0)]
        while st:
            idx,cost = st.pop(0)
            if idx ==goal: return cost
            if idx<0 or idx >1000: continue
            visited[idx] =1
            for a in nums:
                if idx + a ==goal or idx-a ==goal or idx ^a ==goal:
                    return cost+1
                if idx + a >=0 and idx +a <=1000 and visited[idx +a ] ==0:
                    visited[idx+a] =1
                    st.append((idx+a,cost+1))
                if idx - a >=0 and idx -a <=1000 and visited[idx -a ] ==0:
                    visited[idx-a] =1 
                    st.append((idx-a,cost+1))
                if idx ^ a >=0 and idx ^a <=1000 and visited[idx ^a ] ==0:
                    visited[idx^a] =1 
                    st.append((idx ^a,cost+1))
        return mn if find else -1

nums=[-54,25,11,51,-26,46,34,-99,-82,-5,30,90,-55,-81,-48,-91,37,-8,99,15,-100,-92,-44,26,18,49,31,-10,-12,5,-57,-86,-59,17,-95,-72,-46,-15,80,-9,98,66,93,-13,86,-22,29,-88,8,-61,-53,3,16,-40,52,-65,-37,-39,-56,-90,89,36,-84,-64,-1,-58,-24,73,74,-21,45,-89,-93,-77,-76,95,84,-32,40,-83,57,-33]
start=70
goal= 676
re = Solution().minimumOperations(nums , start , goal)
print(re)