import time
import functools

def clock(func):
    @functools.wraps(func)
    def clocked(*args,**kwargs):
        t0 = time.perf_counter()
        result = func(*args,**kwargs)
        elapsed = time.perf_counter() - t0 
        name = func.__name__
        arg_list =[]
        if args:
            arg_list.append( ", ".join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['{0} = {1}'.format(k,w) for k,w in sorted(kwargs.items())]
            arg_list.append(", ".join(pairs))
        arg_str = ", ".join(arg_list)
        print('[{0}] {1}({2}) -> {3}' .format( elapsed, name, arg_str,str(result)))
        return result
    return clocked

@clock
def fx(a,b):
    acc = 0
    mod = 10**9+7
    for i in range(a*100):
        acc += a*b 
    return acc%mod 

if __name__ == "__main__":
    print(fx(10000,b=1023))