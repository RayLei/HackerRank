import math
import os
import random
import re
import sys


#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here

    left = c_q - 1
    right = n - c_q
    upper = n - r_q
    bottom = r_q - 1
    pos_diag = min(n - r_q, n - c_q) + min(r_q - 1, c_q - 1)
    neg_diag = min(n - r_q, c_q - 1) + min(r_q - 1, n - c_q)

    sub_cnt = 0
    for r, c in obstacles:
        # if in the same row
        if r - r_q == 0:
            if c < c_q:
                sub_cnt += c
            elif c > c_q:
                sub_cnt += n - c + 1
        # if in the same column
        elif c - c_q == 0:
            if r > r_q:
                sub_cnt += n - r + 1
            elif r < r_q:
                sub_cnt += r
        # if in positive diagonal
        elif r - r_q == c - c_q:
            if r - r_q > 0:
                sub_cnt += min(n - r + 1, n - c + 1)
            else:
                sub_cnt += min(r, c)
        # if in negative diagonal
        elif r - r_q == c_q - c:
            if r - r_q > 0:
                sub_cnt += min(n - r + 1, c)
            else:
                sub_cnt += min(n - c + 1, r)

    res = left + right + upper + bottom + pos_diag + neg_diag - sub_cnt
    return res

n, k = 5, 3
r_q, c_q = 4, 3
obstacles = [[5, 5],
[4, 2],
[2, 3]]

print(queensAttack(n, k, r_q, c_q, obstacles))
