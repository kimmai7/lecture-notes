lst = [1, 2, 3]
_hidden = iter(lst)
# _hidden -> iterable.__iter__()
# len(_hidden) -> error

for i in range(0, len(lst)):
    print(i)
    # break
else:
    print('else')

class myRange:
    def __init__(self, end):
        self.end = end
        self.count = 0

    def __iter__(self):
        return self
    def __next__(self):
        if self.count == self.end:
            raise StopIteration
        else:
            self.count += 1
            return self.count
        # return self.start

x = myRange(10)
for i in x:
    print(next(x))



# GENERATORS
def myfunction():
    yield # something

def myrange(start, stop, step):
    yield 1
# generator (uses yield)

iter(myrange(1, 3, 1))
print(next(myrange(1, 3, 1)))
x = myrange(1, 3, 1)
print(next(x))
print(next(x))

# tuple comprehension gives you a generator
x = (i for i in 'abc')
print(next(x)) # a
print(next(x)) # b
print(next(x)) # c
print(next(x)) # exception

# def __iter__(self):
#     for i in range(self.start, self.end+1):
#         yield ~



# DEFINITIONS
# iterable: object can be itered, call iter (iterable) -> returns an iterator
# iterator: object can be call on next (repeatedly)
# generator:a special kind of iterator (next on generators)
# generator funcs: a func has one or more yield statement (next)



# COMPARING CLASS OBJECTS
class x:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __lt__(self, other):
        if type(other) is int:
            return self.x < other
        else:
            return self.x < other.x

    def __add__(self, other): # -> self + other
        if type(other) not in (x, int):
            return NotImplemented
        if type(other) is int:
            return x(self.x + other, self.y)
        return x(self.x + other.x, self.y + other.y)
    # print(a + 1)

    def __radd__(self, other): # -> other + self
        if type(other) is int:
            return x(self.x + other, self.y)
        return x(self.x + other.x, self.y + other.y)
    # right add (order matters)

    def __neg__(self):
        return x(-self.x, -self.y)
    # print(-a)

    def __pos__(self):
        return x(abs(self.x), abs(self.y))
    # print(+a2)

    def __eq__(self, other):
        return self.x == other.x # and self.y == other.y
    # print(a == b)

# def __gt__(self, other):
#     self.x > other.x

# using __lt__ and __gt__
a = x(1, 2)
b = x(3, 4)
print(a < 1)
print(a > 1) # -> x -> __gt__ -> __lt__(1, a) (undefined in int type -> does not run)
# python ordering -> __gt__(a, b) -> __lt__(b, a)

# using class funcs
print(a + 1)
print(-a)
a2 = x(-1, -2)
print(+a2)
print(a == b)