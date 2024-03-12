# Modules :-

"""
collection of functions , variables or classes
TWO TYPES :- 1) User defined
             2) Pre defined
Also called as libraries which has functions which can be reused in various programs
File name = module name

"""

# Importing Methods :-
"""
-- import module_name 
            usage -->
                module_name.function_name()
            
-- import module_name as x 
            usage -->
                x.function_name()
            
-- from module_name import function_name
             usage -->
                function_name()
                
-- from module_name import *                                       (* is used to import all functions from that module)
            usage -->
                function_name()
                
-- from module_name import function1_name, function2_name
             usage -->
                function_name()
                
"""

# using MYModule in this program file -->

import MyModule as m

n1 = int(input("\nEnter one integer number : "))
n2 = int(input("\nEnter another integer number : "))
m.sums(n1, n2)
m.sub(n1, n2)
m.div(n1, n2)
m.mul(n1, n2)
