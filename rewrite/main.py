# from algebra.symcollab.algebra.term import Constant, Function, Variable
# from rewrite.symcollab.rewrite import RewriteRule 

from symcollab.algebra import Constant, Function, Variable
from symcollab.rewrite import RewriteRule

from utils import *
import sys



a = Constant("a")
b = Constant("b")
c = Constant("c")
x = Variable("x")
y = Variable("y")
f = Function("f", 2)
g = Function("g", 2)
r = RewriteRule(f(y, g(x, a)), g(y, a))





if __name__=="__main__":
    if len(sys.argv)>1:
        term = sys.argv[1].replace("allpaths","")[1:-1]
        equation = parse_equation(input_str=str(term))
        paths = PathFinder.find_paths(equation) 
        print("term = ",term)
        print("paths = ",paths)
        
    # # Test Case 1
    # term = f(b, g(c, a))
    # equation = parse_equation(input_str=str(term))
    # paths = PathFinder.find_paths(equation) 
    # print("term = ",term)
    # print("paths = ",paths)

    # # Test Case 2

    # print("----------------------------------------------------------------")
    # term  = f(a,b)
    # equation = parse_equation(input_str=str(term))
    # paths = PathFinder.find_paths(equation) 
    # print("term = ",term)
    # print("paths = ",paths)

 