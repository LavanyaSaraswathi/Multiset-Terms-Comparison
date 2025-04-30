
def member_of(x, A):
    return (A.count(x) > 0)

def hd(L):
    if type(L) == type([]):
        if len(L) == 0: return None
        else: return L[0]
    else: return None

def tl(L):
    if type(L) == type([]):
        if len(L) == 0: return None
        else: return L[1:]
    else: return None

def cons(x, L):
    return [x] + L

"""
>>> L = [3, 5, 7]
>>> LL = cons(2, L)
>>> LL
[2, 3, 5, 7]
>>> L
[3, 5, 7]
"""

def mcons(x, L):                      # mutative: changes L
    if type(L) == type([]):
        L.insert(0,x)
        return L
    else: return None
    
def myappend(L1, L2):
    return L1 + L2

def isempty(L):
    return (len(L) == 0)

def rcons(L, x):
    return L + [x]

def eq(x, y):
    return (x == y)

def member(x, L):
    return (x in L)

def general_member(x, L, pred):
    if isempty(L):
        return False
    else:
        y = hd(L)
        if pred(x, y):
            return True
        else:
            return general_member(x, tl(L), pred)

"""
>>> general_member(2, [1,2,3], eq)
True
>>> general_member(2, [3,5,7], eq)
False
"""

generic_member = general_member

def delete(x, L):
    if isempty(L):
        return L
    elif (x == hd(L)):
        return delete(x, tl(L))
    else:
        return cons(hd(L), delete(x, tl(L)))

def rev(L):
    return list(reversed(L))

def sameset(L1, L2):
    return (set(L1) == set(L2))   # works only for simple lists

def listunion(L1, L2):            # works only for simple lists 
    S1 = set(L1)
    S2 = set(L2)
    S3 = S1.union(S2)
    return list(S3)

def list_union_general(L1, L2):
    if isempty(L1):
        return L2
    else:
        if isempty(L2):
            return L1
        else:
            x = hd(L1)
            L3 = list_union_general(tl(L1), L2)
            if member(x, L2):
                return L3
            else:
                return cons(x, L3)

"""
>>> lug = list_union_general
>>> lug([1,3], [2,3,4])
[1, 2, 3, 4]
>>> lug([[1,2], [3], []], [[3], [1]])
[[1, 2], [], [3], [1]]
"""


def generic_union(L1, L2, pred):
    if isempty(L1):
        return L2
    else:
        if isempty(L2):
            return L1
        else:
            x = hd(L1)
            L11 = tl(L1)
            if generic_member(x, L2, pred):
                return generic_union(L11, L2, pred)
            else:
                return [x] + generic_union(L11, L2, pred)
        
"""
>>> L = [1,2,3,4]
>>> M = [2,4,6,8]
>>> generic_union(L, M, eq)
[1, 3, 2, 4, 6, 8]
>>> L
[1, 2, 3, 4]
>>> M
[2, 4, 6, 8]
"""

def listintersect(L1, L2):
    S1 = set(L1)
    S2 = set(L2)
    S3 = S1.intersection(S2)
    return list(S3)

def mapunion(f, L):
    if isempty(L):
        return []
    else:
        return listunion(f(hd(L)), mapunion(f, tl(L)))

def remove_duplicates(L):
    S1 = set(L)
    return list(S1)

def compress(L):
    if isempty(L):
        return []
    else:
        L2 = compress(tl(L))
        if member(hd(L), L2):
            return L2
        else:
            return cons(hd(L), L2)

def generic_compress(L, eqpred):
    if isempty(L):
       return []
    else:
       L2 = generic_compress(tl(L), eqpred)
       if generic_member(hd(L), L2, eqpred):
          return L2
       else:
          return cons(hd(L), L2)

"""
>>> ls = [[1, 3], [1, 3, 2], [3, 1], [2, 3, 1]]
>>> generic_compress(ls, sameset)
[[3, 1], [2, 3, 1]]
"""          

def pos(L, x):                         # leftmost position where x occurs in L
    if member(x, L):
        if x == hd(L):
            return 0
        else: return (1 + pos(tl(L), x))
    else: return (0 - 1)

"""
>>> pos([2,3,5,7,11,13], 7)
3
>>> pos([2,3,5,7,11,13], 8)
-1
"""

def listref(L, x):
    return L[x]

def nth(L, x):
    return L[x]
    

def length(L):
    return len(L)

def listdiff(L1, L2):
    set_difference = set(L1) - set(L2)
    list_difference = list(set_difference)
    return list_difference

"""
>>> L1 = [12, 2, 33]
>>> L2 = [1,2,3]
>>> listdiff(L1, L2)
[33, 12]
>>> L1, L2
([12, 2, 33], [1, 2, 3])
"""

def rev(L):
    return list(reversed(L))

def listrange(L):
    n = len(L)
    return list(range(n))

"""
>>> listrange([12, -2, 300, 100])
[0, 1, 2, 3]
"""

def replace_all(L, a, b):
    if isempty(L):
        return []
    else:
        if (hd(L) == a):
            return cons(b, replace_all(tl(L), a, b))
        else:
            return cons(hd(L), replace_all(tl(L), a, b))

"""
>>> replace_all([1,2,1,3], 1, 10)
[10, 2, 10, 3]
>>> replace_all([2,2,1,3], 1, 10)
[2, 2, 10, 3]
>>> replace_all([2,2,1,3], 2, 10)
[10, 10, 1, 3]
"""

def merge(L1, L2):
    if isempty(L1):
        return L2
    else:
        if isempty(L2):
            return L1
        else:
            if member(hd(L1), L2):
                return merge(tl(L1), L2)
            else:
                return cons(hd(L1), merge(tl(L1), L2))


def add_element_with_flag(x, L):
    if member(x, L):
        return (L, False)
    else:
        return (cons(x, L), True)

"""
>>> ls = [11,23,37,47,59]
>>> add_element_with_flag(17, ls)
([17, 11, 23, 37, 47, 59], True)
>>> ls
[11, 23, 37, 47, 59]
>>> add_element_with_flag(37, ls)
([11, 23, 37, 47, 59], False)
"""


def add_elements_with_flag(ls, L):
    if isempty(ls):
        return (L, False)
    else:
        b = False
        p1 = add_element_with_flag(hd(ls), L)
        L1 = p1[0]
        b1 = b or p1[1]
        p2 = add_elements_with_flag(tl(ls), L1)
        b2 = b1 or p2[1]
        return(p2[0], b2)

"""
>>> add_elements_with_flag([3, 37, 101], ls)
([101, 3, 11, 23, 37, 47, 59], True)
"""

def exists(p, ls):
    if isempty(ls):
        return False
    else:
        return (p(hd(ls)) or (exists(p, (tl(ls)))))

"""
>>> exists(lambda x: (x > 6), [6, 5, 7, 1, 2])
True
>>> exists(lambda x: (x > 6), [6, 5, 4, 1, 2])
False
"""

def forall(p, ls):
    if isempty(ls):
        return True
    else:
        return (p(hd(ls)) and (forall(p, (tl(ls)))))


def copies(x, n):
    if (n < 1):
        return []
    else:
        return cons(x, (copies(x, n - 1)))

n_copies = copies

def update(arrayls, i, x):
    if isempty(arrayls):
        return []
    else:
        if (i == 0):
            return cons(x, tl(arrayls))
        else:
            return cons(hd(arrayls), update(tl(arrayls), i - 1, x))

def same_elements(L1, L2):
    b = True
    for x in L1:
        b = b and (member(x, L2))
    c = True
    for y in L2:
        c = c and (member(y, L1))
    return (b and c)

"""
>>> (ls1, ls2) = ([[1, 2], [3]], [[3], [1,2]])
>>> same_elements(ls1, ls2)
True
"""


def acc(f, ls, initval):
    if isempty(ls):
        return initval
    else:
        x = hd(ls)
        ls2 = tl(ls)
        out = acc(f, ls2, f(initval, x))
    return out

"""
>>> f = lambda a, b : a + b
>>> acc(f, [1,2,3,4,5], 0)
15
"""

def insert_into_sorted_list(x, ls, compfun):
    if isempty(ls):
        return [x]
    else:
        y = hd(ls)
        ls1 = tl(ls)
        if compfun(x, y):
            return cons(y, insert_into_sorted_list(x, ls1, compfun))
        else:
            return cons(x, ls)

"""
>>> compfun = lambda x, y : x > y
>>> insert_into_sorted_list(4, [1,2,3,5], compfun)
[1, 2, 3, 4, 5]
"""

def mysort(ls, compfun):
    if isempty(ls):
        return []
    else:
        if isempty(tl(ls)):
            return ls
        else:
            lss = mysort(tl(ls), compfun)
            return insert_into_sorted_list(hd(ls), lss, compfun)


"""
>>> compfun = lambda x, y : x > y
>>> mysort([10,2,5,11,7,6], compfun)
[2, 5, 6, 7, 10, 11]
"""



def insert_into_t_sorted_list(x, ls, partialfun):
    if isempty(ls):
        return [x]
    else:
        y = hd(ls)
        ls1 = tl(ls)
        if (partialfun(x, y)):
            return cons(x, ls)
        else:
            return cons(y, insert_into_t_sorted_list(x, ls1, partialfun))

"""
>>> from testerfns import *
>>> insert_into_t_sorted_list((3,0), [(1,2), (3,1)], porder1)
[(1, 2), (3, 0), (3, 1)]
"""

def t_sort(ls, partialfun):             # topological sort
    if isempty(ls):
        return []
    else:
        if isempty(tl(ls)):
            return ls
        else:
            lss = t_sort(tl(ls), partialfun)
            return insert_into_t_sorted_list(hd(ls), lss, partialfun)

"""
>>> t_sort(ls, porder1)
[(0, 0), (2, 2), (1, 3), (2, 3), (3, 2)]
"""

def where_they_differ_help(ls1, ls2, p, L):
    if (len(ls1) != len(ls2)):
        return []
    else:
        if isempty(ls1):
            return rev(L)
        else:
            if (hd(ls1) == hd(ls2)):
                return where_they_differ_help(tl(ls1), tl(ls2), p + 1, L)
            else:
                return where_they_differ_help(tl(ls1), tl(ls2), p + 1, cons(p, L))


def where_they_differ(ls1, ls2):
    if (len(ls1) != len(ls2)):
        return []
    else:
        return where_they_differ_help(ls1, ls2, 1, [])


"""
>>> ls1 = [3,4,5]
>>> ls2 = [0,4,5]
>>> where_they_differ(ls1, ls2)
[1]
>>> ls3 = [3,4,6]
>>> where_they_differ(ls1, ls3)
[3]
>>> where_they_differ(ls2, ls3)
[1, 3]
>>> where_they_differ(ls2, [1,2,3,4])
[]
"""

def values_at_positions(ls, indices):
    if isempty(ls):
        return []
    else:
        if isempty(indices):
            return []
        else:
            j = hd(indices)
            if (j < len(ls)):
                return cons(ls[j], values_at_positions(ls, tl(indices)))
            else:
                return values_at_positions(ls, tl(indices))

"""
>>> ls = [2, 3, 5, 7, 11, 13, 17]
>>> len(ls)
7
>>> values_at_positions(ls, [0,2,6])
[2, 5, 17]
>>> values_at_positions(ls, [0,2,6,7])
[2, 5, 17]
"""

def all_occurrences(x, ls):
    if isempty(ls):
        return []
    else:
        newls = all_occurrences(x, tl(ls))
        if (x == hd(ls)):
            return cons(x, newls)
        else:
            return newls

"""
>>> ls = [3, 10, 10, 2, 3, 3]
>>> all_occurrences(10, ls)
[10, 10]
>>> all_occurrences(3, ls)
[3, 3, 3]
"""

def number_of_occurrences(x, ls):
    return len(all_occurrences(x, ls))

def mapcan(f, ls):
    if (ls == []):
       return ls
    else:
       x = f(ls[0])
       ls2 = ls[1:]
       return (x + mapcan(f, ls2))

"""
>>> mapcan(lambda x: [x + 1], [0, 1, 2, 3])
[1, 2, 3, 4]
"""


def minimal_elements(ls, poleq):    # ls must be topologically sorted wrt poleq
    if (len(ls) == 0):
       return ls
    elif (len(ls) == 1):
        return ls
    else:
        ls1 = rev(t_sort(ls, poleq))
        x = ls1[0]
        ls2 = minimal_elements(ls1[1:], poleq)
        if any(map(lambda y: poleq(y, x), ls2)):
           return ls2
        else:
           return cons(x, ls2)

"""
>>> minimal_elements([[1, 2], [1, 2, 3], [1, 3]], subseteq)
[[1, 2], [1, 3]]
>>> minimal_elements([[1, 2], [1, 2, 3], [1, 3]], supseteq)
[[1, 2, 3]]
"""

def minimal_elements2(ls, poleq):
   if (len(ls) == 0):
      return ls
   else:
      n = len(ls)
      for i in range(n):
        for j in range(i+1, n):
          if (ls[i] == None):
             break
          if (poleq(ls[i], ls[j])):
             ls[j] = ls[i]
             ls[i] = None
          elif (poleq(ls[j], ls[i])):
             ls[i] = None
      return delete(None, ls)

"""
>>> minimal_elements2([[1, 2, 3], [1, 2], [2], [1, 3]], subseteq)
[[2], [1, 3]]
>>> minimal_elements2([[1, 2], [1, 2, 3], [1, 3]], subseteq)
[[1, 2], [1, 3]]
>>> minimal_elements2([[1, 2, 3], [1, 3], [4], [1, 4]], subseteq)
[[1, 3], [4]]
>>> minimal_elements2([[1, 2, 3], [4], [1, 3], [3], [1, 4]], subseteq)
[[3], [4]]
"""

def delete_leftmost(x, ls):
    if isempty(ls):
        return []
    elif (x == ls[0]):
        return ls[1:]
    else:
        return cons(ls[0], delete_leftmost(x, ls[1:]))

"""
>>> ls = [1, 2, 1, 2, 3, 33]
>>> delete_leftmost(1, ls)
[2, 1, 2, 3, 33]
>>> ls
[1, 2, 1, 2, 3, 33]
>>> delete_leftmost(2, ls)
[1, 1, 2, 3, 33]
"""

def subsequence(ls1, ls2):
    if (len(ls1) == 0):
        return True
    elif (len(ls2) == 0):
        return False
    else:
        x = hd(ls1)
        y = hd(ls2)
        ls11 = tl(ls1)
        ls21 = tl(ls2)
        if (x == y):
            return subsequence(ls11, ls21)
        else:
            return subsequence(ls1, ls21)

"""
>>> subsequence([1,3,4,7], [1,2,3,4,5,6,7])
True
>>> subsequence([1,3,4,7], [1,2,3,4,5,6])
False
>>> subsequence([1,3,4,7], [2,1,3,1,4,7])
True
"""




 
