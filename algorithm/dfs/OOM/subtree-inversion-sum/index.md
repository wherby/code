## DFS too many state

## Use cache 

use Cache will fail in python 3.14 : 

(base) tao@MacBook-Pro code % /usr/local/bin/python3 /Users/tao/software/code/contest/00000c443d154/d156/q4/t4.py
Fatal Python error: _Py_CheckRecursiveCall: Unrecoverable stack overflow (used 3929 kB) in comparison
Python runtime state: initialized

In python 3.12 in Mac the recurring setting will not be  applied:

           ^^^^^^^^^^^^^^^^^^^^^^
  [Previous line repeated 28 more times]
RecursionError: maximum recursion depth exceeded


in Python 3.9.6:

(base) tao@MacBook-Pro code % /usr/bin/python3 /Users/tao/software/code/algorithm/dfs/OOM/subtree-inversion-sum/dfsStackOverflow.py
zsh: segmentation fault  /usr/bin/python3 

## Use mem

in python 3.9.6

(base) tao@MacBook-Pro code % /usr/bin/python3 /Users/tao/software/code/algorithm/dfs/OOM/subtree-inversion-sum/oneTimeDFSWithMemAC.py
zsh: segmentation fault  /usr/bin/python3 

in python 3.12.5 will work

(base) tao@MacBook-Pro code % /usr/local/bin/python3.12 /Users/tao/software/code/algorithm/dfs/OOM/subtree-inversion-sum/oneTimeDFSWithMemAC.py
2500000000

in python 3.14 will work

(base) tao@MacBook-Pro code % /usr/local/bin/python3 /Users/tao/software/code/algorithm/dfs/OOM/subtree-inversion-sum/oneTimeDFSWithMemAC.py
2500000000