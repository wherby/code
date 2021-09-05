import bisect


def query(arr, left, right):
    jx = bisect.bisect(arr, right)
    ix = bisect.bisect_left(arr, left)
    return jx - ix


ls = [2,3,5,6,7,8,9,10]
print(query(ls, 4,10))
print(query(ls,3,11))