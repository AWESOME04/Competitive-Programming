#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    value_to_insert = arr[-1]
    position = n - 2  

    while position >= 0 and arr[position] > value_to_insert:
        arr[position + 1] = arr[position]
        print(*arr)  
        position -= 1

    arr[position + 1] = value_to_insert
    print(*arr)  

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)
    

    
    
    
    
    
