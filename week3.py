# UNIT TIME
# func printing a very long list
def p(lst):
    print(lst)
# unit time = 1
# graph: constant straight horizontal line

def p2(lst):
    for i in lst:
        print(i)
# graph: linear relationship
# calls each element in the list



# BIG O NOTATION
# measures the efficiency

# fibonacci sequence
# o notation: jn (exponential growth)
def f(n):
    return f(n-1) + f(n-2)



# LINKED LISTS
# need to reverse the order
class LinkedList:
    def __init__(self, n, next):
        self.n = n
        self.next = next
# [1, next] -> [2, next] -> [3, next] -> [4, None]