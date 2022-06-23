#https://leetcode-cn.com/problems/mini-parser/

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """
       self.values = []
       if value != None:
           self.values = [value]
    def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """
       return len(self.values) ==1

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        self.values.append(elem)

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        self.values[0] = value

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        if len(self.values) ==1:
            return self.values[0]
        else:
            return None

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        if len(self.values) ==1:
            return None
        else:
            return self.values
        
    def __repr__(self):
        if self.isInteger():
            return str(self.values[0])
        else:
            strs = [str(a) for a in self.values]
            return "[" +",".join(strs) +"]"

    def __str__(self):
        if self.isInteger():
            return str(self.values[0])
        else:
            strs = [str(a) for a in self.values]
            return "[" +"".join(strs) +"]"
        #return "From str method of Test: a is %s" % (self.values)
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        index = 0

        def dfs() -> NestedInteger:
            nonlocal index
            if s[index] == '[':
                index += 1
                ni = NestedInteger()
                while s[index] != ']':
                    ni.add(dfs())
                    if s[index] == ',':
                        index += 1
                index += 1
                return ni
            else:
                negative = False
                if s[index] == '-':
                    negative = True
                    index += 1
                num = 0
                while index < len(s) and s[index].isdigit():
                    num *= 10
                    num += int(s[index])
                    index += 1
                if negative:
                    num = -num
                return NestedInteger(num)

        return dfs()

s = "[123,[456,[-789]]]"
re = Solution().deserialize(s)
print(re.getList())