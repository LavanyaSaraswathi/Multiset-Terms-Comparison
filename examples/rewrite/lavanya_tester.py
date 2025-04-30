# from algebra.symcollab.algebra.term import Constant, Function, Variable
# from rewrite.symcollab.rewrite import RewriteRule 

from signature import *

from utils import *

from path_ordering import *

import sys

def enumerate_paths(term):
    paths = parse_equation(str(term))
    return paths

"""
$ python3 -m venv senv
cryptosolve 6$ source senv/bin/activate
(senv) cryptosolve 7$ cd ..
(senv) python 9$ python3 -i lavanya_tester.py 
>>> enumerate_paths(f(a, h(b)))
[['f', 'a'], ['f', 'h', 'b']]
>>> enumerate_paths(f(f(x, y), z))
[['f', 'f', 'x'], ['f', 'f', 'y'], ['f', 'z']]
>>> enumerate_paths(f(f(z, z), z))
[['f', 'f', 'z'], ['f', 'f', 'z'], ['f', 'z']]
>>> enumerate_paths(f(f(z, z), h(z)))
[['f', 'f', 'z'], ['f', 'f', 'z'], ['f', 'h', 'z']]
>>> enumerate_paths(f(h(f(x, y)), h(z)))
[['f', 'h', 'f', 'x'], ['f', 'h', 'f', 'y'], ['f', 'h', 'z']]
>>> enumerate_paths(f(f(z, h(h(h(z)))), h(z)))
[['f', 'f', 'z'], ['f', 'f', 'h', 'h', 'h', 'z'], ['f', 'h', 'z']]
"""

def symbol_ordering(ls):
    return list(map(str, ls))

def compare_terms(term1, term2, ascending):
    plist1 = parse_equation(str(term1))
    plist2 = parse_equation(str(term2))
    symorder = symbol_ordering(ascending)
    return poms(plist1, plist2, symorder)

"""
>>> t1 = f(h(x), h(y))
>>> t2 = f(g(x, y), g(x, y))
>>> compare_terms(t1, t2, [g, h, f])
True
>>> t3 = f(g(x, y), g(x, h(y)))
>>> compare_terms(t1, t3, [g, h, f])
False
"""

