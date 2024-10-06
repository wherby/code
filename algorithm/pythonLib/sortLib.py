# python 用sort 如果需要定义排序算法需要两个值，需要用 cmp_to_key(compare) 定义key,这样可以使用微扰贪心算法
# 求最大字典序列
from functools import cmp_to_key
def compare(a,b):
    print(a,b, a+b,b+a,a+b>b+a)
    return int(a+b) -int(b+a)

def sortArr(ls):
    ls = sorted(ls,key =cmp_to_key(compare),reverse=True)
    return "".join(ls)

ls = ["8","81","82","829"]
print(sortArr(ls))