#HackerRank --PrepareData StructuresArrays2D Array - DS 
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    max= -float('inf')
    for i in range(1,5):
        for j in range(1,5):
            sum =0
            sum+=arr[i][j]
            sum+=arr[i-1][j-1]+arr[i-1][j]+arr[i-1][j+1]
            sum+=arr[i+1][j-1]+arr[i+1][j]+arr[i+1][j+1]
            
            if(sum>max):
                max=sum
    
    return max        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
