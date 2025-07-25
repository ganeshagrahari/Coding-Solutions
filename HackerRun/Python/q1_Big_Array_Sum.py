'''
In this challenge, you need to calculate and print the sum of elements in an array, considering that some integers may be very large.

Function Description

Complete the  function with the following parameter(s):

: an array of integers
Return

: the sum of the array elements
Input Format

The first line of the input consists of an integer .
The next line contains  space-separated integers contained in the array.

Output Format

Return the integer sum of the elements in the array.

Constraints


Sample Input

STDIN                                                   Function
-----                                                   --------
5                                                       arr[] size n = 5
1000000001 1000000002 1000000003 1000000004 1000000005  arr[...]  
Output

5000000015
Note:

The range of the 32-bit integer is .

When we add several integer values, the resulting sum might exceed the above range. You might need to use long int C/C++/Java to store such sums.'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

def aVeryBigSum(ar):
    # Write your code here
    total =0
    for i in ar:
        total+=i
    return total    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
