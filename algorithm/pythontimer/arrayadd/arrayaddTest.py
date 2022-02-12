
from time import time
import collections
  
def timer_func(func):
    # This function shows the execution time of 
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func
  

@timer_func
def arrayAdd(num):
    arr = []
    for _ in range(1000):
        tmp = []
        for j in range(num): 
            tmp.append(j)
        arr.append(tmp)
    return arr

@timer_func
def queueAdd(num):
    arr = []
    for _ in range(1000):
        tmp = collections.deque([])
        for j in range(num): 
            tmp.append(j)
        arr.append(tmp)
    return arr


@timer_func
def arrayAddRemove(num):
    arr = []
    for _ in range(1000):
        tmp = []
        for j in range(num): 
            tmp.append(j)
        for _ in range(num):
            tmp.pop(0)
        arr.append(tmp)
    return arr

@timer_func
def queueAddRemove(num):
    arr = []
    for _ in range(1000):
        tmp = collections.deque([])
        for j in range(num): 
            tmp.append(j)
        for _ in range(num):
            tmp.popleft()
        arr.append(tmp)
    return arr

num = 10000
arrayAdd(num)
queueAdd(num)
arrayAddRemove(num)
queueAddRemove(num)