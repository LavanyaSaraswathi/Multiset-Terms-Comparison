
from listfns import *

def delete_common(ls1, ls2):
    if isempty(ls2):
        return (ls1, ls2)
    elif (ls2[0] in ls1):
        ls11 = delete_leftmost(ls2[0], ls1)
        ls22 = ls2[1:]
        return delete_common(ls11, ls22)
    else:
        (ls3, ls4) = delete_common(ls1, ls2[1:])
        return (ls3, cons(ls2[0], ls4))

"""
>>> delete_common([1,2,3,3,4,4,4], [4, 2, 2, 1, 3])
([3, 4, 4], [2])
"""

def mcompare(ls1, ls2, wpo):
    (L1, L2) = delete_common(ls1, ls2)
    if isempty(L1):
        return False
    elif isempty(L2):
        return True
    else:
        x = L2[0]
        if exists(lambda y: wpo(y, x), L1):
            return mcompare(ls1, ls2[1:], wpo)
        else:
            return False

def gt(x, y):
    return (x > y)

"""
>>> mcompare([1,2,3,3,4,4,4], [4, 2, 2, 1, 3], gt)
True
>>> mcompare([1,2,3,3,4,4,4], [4, 2, 5, 1, 3], gt)
False
"""


