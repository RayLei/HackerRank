import math
import os
import random
import re
import sys


#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    dict_cnt = {}
    for x in s:
        dict_cnt[x % k] = 1 + dict_cnt.get(x % k, 0)

    res = 0 if 0 not in dict_cnt.keys() else 1
    for i in range(1, k):
        if i * 2 == k:
            res += 1
        else:
            res += max(dict_cnt.get(i, 0), dict_cnt.get(k-i, 0))
            dict_cnt[i] = dict_cnt[k-i] = 0
    return res


s = list(map(int, '278 576 496 727 410 124 338 149 209 702 282 718 771 575 436'.split(' ')))
k = 7

print(nonDivisibleSubset(k, s))
