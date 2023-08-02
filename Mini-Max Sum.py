#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    print(arr)
    x=reduce(lambda x,y:x+y,arr[:4])
    y=reduce(lambda x,y:x+y,arr[:0:-1])
    print(x,y)
# Write your code here


if __name__ == '__main__':
    arr = [7,69,2,221,8974]

    miniMaxSum(arr)
