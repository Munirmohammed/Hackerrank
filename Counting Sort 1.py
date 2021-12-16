#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

n = int(input())
munir = list(map(int, input().split()))

total = [0]*100

for j in range(0,n):
    temp = munir[j]
    total[temp] += 1
print(*total, sep =' ')

