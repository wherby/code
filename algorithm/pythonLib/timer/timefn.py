import time


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0 
        name = func.__name__
        arg_str = ", ".join(repr(arg) for arg in args)
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
    print(fx(10000,1023))