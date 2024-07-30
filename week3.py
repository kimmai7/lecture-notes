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



class C:
    def __init__(self, x, y):
        self.lst = [x, y]

    def len(self):
        return len(self.lst)

    def __len__(self):
        return len(self.lst)

a = C(1, 2)
print(len(a))
# this will only work if the len func is a dunder method
# otherwise it doesn't know there is a len func in the class C

print(a.__dict__)
a.x = 1
a.__dict__['y'] = 2
print(a.y)

# BBUS