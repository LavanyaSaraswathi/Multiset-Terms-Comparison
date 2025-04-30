
from listfns import *

from multisets import *

def find_common_suffix(ls1, ls2):
    suffix = []
    for i in range(1, min(len(ls1), len(ls2))+1):
        if ls1[-i] == ls2[-i]:
            suffix = cons(ls1[-i], suffix)
        else:
            break
    return suffix

"""
>>> find_common_suffix([1,4,2,5], [3,2,5])
[2, 5]
>>> find_common_suffix([1,4,2,5], [3,2,6])
[]
"""

def remove_common_suffix(s1, s2):
    suffix = find_common_suffix(s1, s2)
    if (len(suffix) == 0):
        return (s1, s2)
    else:
        return (s1[:-len(suffix)], s2[:-len(suffix)])

"""
>>> remove_common_suffix([1,4,2,5], [3,2,5])
([1, 4], [3])
>>> remove_common_suffix([1,4,2,5], [3,2,6])
([1, 4, 2, 5], [3, 2, 6])
"""

def remove_common_prefix(ls1, ls2):
    if ((len(ls1) == 0) or (len(ls2) == 0)):
        return (ls1, ls2)
    elif (ls1[0] != ls2[0]):
        return (ls1, ls2)
    else:
        return remove_common_prefix(tl(ls1), tl(ls2))

"""
>>> remove_common_prefix([1,4,2,5], [3,2,6])
([1, 4, 2, 5], [3, 2, 6])
>>> remove_common_prefix([1,4,2,5], [1,2,6])
([4, 2, 5], [2, 6])
"""

def rpo_on_lists(ls1, ls2, ascending):
    (ls3, ls4) = remove_common_suffix(ls1, ls2)
    (x, y) = remove_common_prefix(ls3, ls4)
    if (len(x) == 0):
        return False
    elif (len(y) == 0):
        return True
    else:
        f = hd(x)
        g = hd(y)
        if (pos(ascending, f) > pos(ascending, g) >= 0):
            return rpo_on_lists(x, tl(y), ascending)
        elif (tl(x) == y):
            return True
        else:
            return rpo_on_lists(tl(x), y, ascending)

"""
>>> rol = rpo_on_lists
>>> rol(['a', 'b', 'a', 'c'], ['b', 'b', 'c'], ['c', 'b', 'a'])
True
>>> rol(['b', 'b', 'a', 'c'], ['a', 'b', 'c'], ['c', 'b', 'a'])
False
>>> rol(['b', 'b', 'a', 'c'], ['b', 'c'], ['c', 'b', 'a'])
True
"""

def rpofn_given_ascending(ascending):
    return lambda x, y : (rpo_on_lists(x, y, ascending))

"""
>>> rpoga = rpofn_given_ascending
>>> f = rpoga(['c', 'b', 'a'])
>>> f(['a', 'b', 'a', 'c'], ['b', 'b', 'c'])
True
>>> f(['b', 'b', 'a', 'c'], ['a', 'b', 'c'])
False
>>> f(['b', 'b', 'a', 'c'], ['b', 'a', 'c'])
True
>>> f(['g', 'a', 'd', 'X'], ['g', 'b', 'b', 'X'])
True
>>> f(['g', 'a', 'X'], ['g', 'b', 'b', 'Y'])
False
"""

def path_ordering_multisets(lls1, lls2, ascending):
    f = rpofn_given_ascending(ascending)
    return mcompare(lls1, lls2, f)

poms = path_ordering_multisets

"""
>>> lpaths1 = [['f', 'g', 'X'], ['f', 'g', 'X'], ['f', 'g', 'Y'], ['f', 'g', 'Y']]
>>> lpaths2 = [['f', 'h', 'X'], ['f', 'h', 'Y'], ['f', 'h', 'X'], ['f', 'h', 'Y']]
>>> poms(lpaths1, lpaths2, ['h', 'g', 'f'])
True
"""




        



 
