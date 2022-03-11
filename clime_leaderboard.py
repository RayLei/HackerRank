import math
import os
import random
import re
import sys

def climbingLeaderboard(ranked, player):
    # Write your code here
    ranked.insert(0, math.inf)
    ranked.append(-math.inf)

    dict_rank = {}
    init, prv_rank = 0, math.inf
    for i, r in enumerate(ranked):
        if r < prv_rank:
            init += 1
            prv_rank = r
            dict_rank[r] = init
    dict_rank[math.inf] = 0

    l, r = 0, len(ranked) - 1
    res = []
    for p in player:
        l = 0
        found = False
        while l + 1 < r:
            mid = (l + r) // 2
            if p > ranked[mid]:
                r = mid
            elif p < ranked[mid]:
                l = mid
            else:
                res.append(dict_rank[p])
                found = True
                break
        if not found:
            res.append(dict_rank[ranked[r]])
    return res


ranked = [100, 100, 50, 40, 40, 20, 10]
player = [5, 25, 50, 120]

print(climbingLeaderboard(ranked, player))
