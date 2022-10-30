# https://leetcode.cn/problems/sum-of-subarray-minimums/submissions/
class Solution:
    def sumSubarrayMins(self, arr) -> int:
        n =len(arr)
        st =[(0,-1)]
        left = [0]*n
        for i,a in enumerate(arr):
            while a < st[-1][0]:
                st.pop()
            left[i] = i - st[-1][1]
            st.append((a,i))
        right =[0]*n 
        st =[(0,-1)]
        for i,a in enumerate(arr[::-1]):
            while a <= st[-1][0]:
                st.pop()
            right[n-i-1] = i - st[-1][1]
            st.append((a,i))
        acc =0
        for i in range(n):
            acc += arr[i] * left[i]*right[i]
        mod = 10**9 +7
        #print(left,right)
        acc =acc % mod 
        return acc
re =Solution().sumSubarrayMins([71,55,82,55])
print(re)