
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoNumberSum' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER target
#

def twoNumberSum(arr, target):
    # Write your code here
    nums = {}
    for num in arr:
        potentialMatch = target - num
        if potentialMatch in nums:
            return [potentialMatch,num]
        else:
            nums[num] = True
    
    return [-1]



if __name__ == '__main__':


    arr = [2,3,4,5,6,9]
    
    target = 10

    result_array = twoNumberSum(arr, target)

    print(result_array)
