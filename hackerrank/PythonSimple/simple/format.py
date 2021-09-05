#!/bin/python
#https://www.hackerrank.com/challenges/plus-minus/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
from __future__ import print_function

import os
import sys

#
# Complete the plusMinus function below.
#
def plusMinus(arr):
    #
    # Write your code here.
    #
    pls = filter(lambda x: x>0,arr)
    nls = filter(lambda x: x<0,arr)
    a1= (len(pls))*1.0/len(arr)
    b1=(len(nls))*1.0/len(arr)
    c1 = (len(arr)-len(pls)-len(nls))*1.0/len(arr)
    print("{:.6f}".format(a1))
    print("{:.6f}".format(b1))
    print("{:.6f}".format(c1))
    
if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    plusMinus(arr)