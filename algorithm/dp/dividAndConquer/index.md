
## https://www.quora.com/What-is-divide-and-conquer-optimization-in-dynamic-programming
``` python
def ComputeDP(i, jleft, jright, kleft, kright): 
  # Select the middle point 
  jmid = (jleft + jright) / 2 
  # Compute the value of dp[i][jmid] by definition of DP 
  dp[i][jmid] = +INFINITY 
  bestk = -1 
  for k in range(kleft, jmid): 
    if dp[i - 1][k] + C[k + 1][jmid] < best: 
      dp[i][jmid] = dp[i - 1][k] + C[k + 1][jmid] 
      bestk = k 
  # Divide and conquer 
  if jleft < jmid - 1: 
    ComputeDP(i, jleft, jmid - 1, kleft, bestk) 
  if jleft + 1 < jright: 
    ComputeDP(i, jmid + 1, jright, bestk, kright) 
 
def ComputeFullDP: 
  Initialize dp for i = 0 somehow 
  for i in range(1, m): 
    ComputeDP(i, 0, n, 0, n) 
```

## https://cp-algorithms.com/dynamic_programming/divide-and-conquer-dp.html#generic-implementation