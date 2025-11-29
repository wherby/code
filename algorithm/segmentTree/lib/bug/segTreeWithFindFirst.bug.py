from typing import List, Tuple, Optional
from math import inf

class SegmentTree:
    def __init__(self, op=max, e=lambda: -float("inf"), a=[]):

        self.n = n = len(a)
        self.op, self.e = op, e
        self.leafN = 1
        while n > self.leafN:
            self.leafN <<= 1
        self.offset = self.leafN

        self.x = [e for _ in range(self.leafN << 1)]
        if a:
            self.x[self.offset : self.offset + n] = a[:]
            l = self.offset
            r = l + self.leafN
            while 1 < l:
                for i in range(l, r, 2):
                    self.x[i >> 1] = op(self.x[i], self.x[i + 1])
                l >>= 1
                r >>= 1

    def get_value(self, i):

        return self.x[self.offset + i]

    def tolist(self):
        res = []
        for i in range(self.n):
            res.append(self.get_value(i))
        return res

    def set_value(self, i, val):

        i += self.offset
        self.x[i] = val
        while 1 < i:
            i >>= 1
            j = i << 1
            self.x[i] = self.op(self.x[j], self.x[j + 1])

    def prod(self, l, r):

        l += self.offset
        r += self.offset
        val_l, val_r = self.e, self.e
        while l < r:
            if l & 1:
                val_l = self.op(val_l, self.x[l])
                l += 1
            if r & 1:
                r -= 1
                val_r = self.op(self.x[r], val_r)
            l >>= 1
            r >>= 1
        return self.op(val_l, val_r)

    # max_right(self, i, check_func): Finds the maximum index j such that check_func returns True for the range [i, j).
    def max_right(self, i, check_func):

        i += self.offset
        if not check_func(self.x[i]):
            return -1
        val_l = self.e
        while True:
            i //= i & -i
            temp = self.op(val_l, self.x[i])
            if not check_func(temp):
                while i < self.offset:
                    i <<= 1
                    temp = self.op(val_l, self.x[i])
                    if check_func(temp):
                        val_l = temp
                        i += 1
                return i - 1 - self.offset
            val_l = temp
            i += 1
            if i & -i == i:
                return self.n - 1
    # min_left(self, j, check_func): Finds the minimum index i such that check_func returns True for the range [i, j).
    def min_left(self, j, check_func):

        j += self.offset
        if not check_func(self.x[j]):
            return -1
        val_r = self.e
        while True:
            j += 1
            j = j // (j & -j) - 1
            temp = self.op(self.x[j], val_r)
            if not check_func(temp):
                while j < self.offset:
                    j = (j << 1) + 1
                    temp = self.op(self.x[j], val_r)
                    if check_func(temp):
                        j -= 1
                        val_r = temp
                return j + 1 - self.offset
            val_r = temp
            if j & -j == j:
                return 0
            j -= 1

    def min_right(self, i, check_func):

        ret = self.max_right(i, lambda x: not check_func(x))
        if ret == self.n - 1:
            return -1
        if ret < 0:
            return i
        return ret + 1

    def max_left(self, j, check_func):

        ret = self.min_left(j, lambda x: not check_func(x))
        if ret < 0:
            return j
        return ret - 1

    def __setitem__(self, k: int, key):
        self.set_value(k, key)

    def __getitem__(self, k: int):
        return self.get_value(k)

    def __len__(self):
        return self.n

    def __str__(self):
        return str(self.tolist())

    def __bool__(self):
        return self.n != 0

    def __repr__(self):
        return f"SegmentTree({self.tolist()})"



class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        st = SegmentTree(op=max, e=-inf, a=baskets)
        n = len(baskets)
        
        print("minright：idx 开始 最左一个符合条件的")
        for f in fruits:
            k = st.min_right(0,lambda x :x>=f)
            print(k,f,)
        print("maxright：从左 idx 开始 到右找到最后一个符合条件的，下一个(右一个)是第一次不符合")
        for f in fruits:
            k = st.max_right(4,lambda x :x<f)
            print(k,f,"<")
        for f in fruits:
            k = st.max_right(0,lambda x :x<=f)
            print(k,f,"<=")
        print("minleft:从右idx到左找到最后一个符合条件的，左一个第一个是不符合 ***BUG***")
        for f in fruits:
            k = st.min_left(n-1,lambda x :x<=f)
            print(k,f,)
        print("maxleft: 从idx开始最右第一个符合条件的")
        for f in fruits:
            k = st.max_left(n-1,lambda x :x>=f)
            print(k,f,"maxleft")
            
re =Solution().numOfUnplacedFruits(fruits = [4,2,5,6,1,0], baskets = [1,3,5,4,2,5,4,5,4,2,1])


# Class Overview
# __init__(self, op=max, e=lambda: -float("inf"), a=[]): Initializes the segment tree.

# op: The operation to be performed on the segments (default is max).

# e: The identity element for the operation (default is -infinity).

# a: The initial array of values (default is an empty list).

# get_value(self, i): Returns the value at index i.

# tolist(self): Converts the segment tree to a list.

# set_value(self, i, val): Sets the value at index i to val.

# prod(self, l, r): Returns the result of the operation op applied to the range [l, r).

# max_right(self, i, check_func): Finds the maximum index j such that check_func returns True for the range [i, j).

# min_left(self, j, check_func): Finds the minimum index i such that check_func returns True for the range [i, j).

# min_right(self, i, check_func): Finds the minimum index j such that check_func returns True for the range [i, j).

# max_left(self, j, check_func): Finds the maximum index i such that check_func returns True for the range [i, j).

# __setitem__(self, k, key): Allows setting values using the [] notation.

# __getitem__(self, k): Allows getting values using the [] notation.

# __len__(self): Returns the number of elements in the segment tree.

# __str__(self): Returns a string representation of the segment tree.

# __bool__(self): Returns True if the segment tree is not empty.

# __repr__(self): Returns a detailed string representation of the segment tree.


# how to find min index of array which is greater than a value?
# To find the minimum index in an array where the value is greater than a given value, you can use the min_right method of the SegmentTree class. This method is specifically designed for such queries.

# Here’s how you can do it:

# Steps:
# Define a check function that checks if a value is greater than the given value.

# Use the min_right method to find the smallest index j such that the value at j is greater than the given value.

# # Initialize a segment tree with an array and the max operation
# a = [1, 3, 2, 7, 9, 11]
# st = SegmentTree(op=max, e=lambda: -float("inf"), a=a)

# # Define the value to compare against
# value = 5

# # Define the check function
# def check_func(x):
#     return x > value

# # Find the minimum index j where a[j] > value
# min_index = st.min_right(0, check_func)

# # Output the result
# if min_index == -1:
#     print("No such index exists")
# else:
#     print(f"The minimum index where the value is greater than {value} is: {min_index}")
# Explanation:
# check_func(x): This function returns True if x > value. It is used to determine if a value in the array satisfies the condition.

# min_right(0, check_func): This method starts searching from index 0 and finds the smallest index j where a[j] > value. If no such index exists, it returns -1.

# Example Walkthrough:
# For the array [1, 3, 2, 7, 9, 11] and value = 5:

# The values greater than 5 are 7, 9, and 11.

# The smallest index where the value is greater than 5 is 3 (value 7).

# Output:

# Copy
# The minimum index where the value is greater than 5 is: 3
# Edge Cases:
# If no value in the array is greater than the given value, the result will be -1.

# If the array is empty, the result will also be -1.

# Complexity:
# The min_right method operates in O(log n) time, making it efficient for large arrays.

# This approach is efficient and leverages the power of the segment tree for range queries.


class Solution2:
    def leftmostBuildingQueries(self, a: List[int], queries: List[List[int]]) -> List[int]:
        # st = SparseTable(a, max)
        # # 记录最后一次的位置
        # d = {}
        # for i, ai in enumerate(a):
        #     d[ai] = i
        st = SegmentTree(op=max, e=-inf, a=a)
        
        res = []
        for l, r in queries:
            if l>r:
                l, r = r, l
            if l==r:
                res.append(l)
                continue
            i = st.min_right(r, lambda vx: vx>a[l])
            
            res.append(i)
        return res