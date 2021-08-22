
class Stack:
    """模拟栈"""
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return len(self.items)==0 
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop() 
    
    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items)-1]
        else:
            return 1000000000
        
    def size(self):
        return len(self.items) 

class Solution(object):
    def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        st =Stack()
        res = [0]*len(heights)
        n =len(heights)
        for i in range(len(heights)):
            t = heights[n-1-i]
            cnt =0
            if st.isEmpty():
                st.push(t)
            else:
                while t > st.peek():
                    st.pop()
                    cnt = cnt +1
                if not st.isEmpty():
                    cnt = cnt +1
                res[n-1-i] =cnt
                st.push(t)
        return res

a = Solution().canSeePersonsCount([10,6,8,5,11,9])
print(a)