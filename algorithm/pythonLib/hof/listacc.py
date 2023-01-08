
from itertools import accumulate

def testAcc(stations,radius):
    accumulated_sum = list(accumulate(stations, initial=0))
    print(accumulated_sum)
    n = len(stations)
    current = [accumulated_sum[min(i+radius+1, n)] - accumulated_sum[max(i-radius, 0)] for i in range(n)]
    print(current)

stations = [1,2,3,4,5,6,7,8]
testAcc(stations,1)