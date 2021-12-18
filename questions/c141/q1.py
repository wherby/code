class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        st =[]
        n = len(arr)
        for a in arr:
            st.append(a)
            if a ==0:
                st.append(0)
        while len(st)> n:
            st.pop()
        for i in range(n-1,-1,-1):
            arr[i] = st.pop()
        print(arr)

re = Solution().duplicateZeros([1,0,2,3,0,4,5,0])
        

        