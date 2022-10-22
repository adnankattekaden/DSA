#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'validSubSequence' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY sequence
#

def validSubSequence(arr, sequence):
    seqIdx = 0
    for value in arr:
        if seqIdx == len(sequence):
            break

        
        if sequence[seqIdx] == value:
            seqIdx += 1

    
    return seqIdx == len(sequence)

if __name__ == '__main__':
    

    arr = [2,4,5,6,7,9,3,1,8,10,4,6,9,8]

    sequence = [5,10,22,3]

    check = validSubSequence(arr, sequence)

    print(check)