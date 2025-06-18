
# 矩阵反转
a = [[1,2],[3,4]]
b = list(zip(*a))
print(b)

#数列order顺序
nums = [3,2,4,5,1,0]
n = len(nums)
order = sorted(range(n), key=lambda x: nums[x])