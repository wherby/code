
# 矩阵反转



a = [[1,2],[3,4]]
b = list(zip(*a))
print(b)

#数列order顺序
nums = [3,2,4,5,1,0]
n = len(nums)
order = sorted(range(n), key=lambda x: nums[x])

# 求欧式距离
# >>> import math
# >>> math.hypot(1,1)
# 1.4142135623730951
# >>> math.hypot(1,1,1)
# 1.7320508075688772
# >>> math.hypot(1,1,1,2)
# 2.6457513110645907
# >>> math.hypot(1,1,1,1)
# 2.0

# groupby
from itertools import groupby
str = "leeettcoodde"
for a,group in groupby(str):
    print(a,list(group))

# l ['l']
# e ['e', 'e', 'e']
# t ['t', 't']
# c ['c']
# o ['o', 'o']
# d ['d', 'd']
# e ['e']