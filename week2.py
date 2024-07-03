# POSITIONAL & KEYWORD ARGS
def foo(a, b, **kwargs):
    print(a, b, kwargs)

foo(c = 3, a = 1, b = 2, d = 4)
# returns 1 2 {'c': 3, 'd': 4}
# positioning of variables doesn't matter
foo (1, 2, c = 3, d = 4)
# returns (1, 2) {'c': 3, 'd': 4}
foo(a = 1, b = 2, c = 3, d = 4)
# returns () {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print()


def h(a, b, c, d):
    print(a, b, c, d)
def i(*args, **kwargs):
    h(*args, **kwargs)

i(1, 2, c = 3, d = 4)
# returns 1 2 3 4
i(a = 1, b = 2, c = 3, d = 4)
# also returns 1 2 3 4
print()


# NESTED FUNCS
def bigger_than(age):
    def test_it(x):
        return x > age
    return test_it

old = bigger_than(80)
print(old(85))
# returns True
# old is stored as a test_it() func, so x = 85 and age = 80

def f():
    prev = None
    def g1(x):
        nonlocal prev
        temp = prev
        prev = x + 5
        return temp
    def g2(x):
        nonlocal prev
        temp = prev
        prev = x * 5
        return temp
    return g1, g2

f1, f2 = f()
print(f1(1))
print(f2(1))
# returns None, 6
print()


# LAMBDA FUNC
def add(a, b):
    return a + b

print(add(3, 4))
print((lambda x, y: x + y))
print((lambda x, y: x + y)(3, 4))

add2 = (lambda x, y: x + y)
print(add2(5, 6))

def bigger_than_age(age):
    return (lambda x: x > age)
print()


# LIST COMPREHENSION
lst = []
for i in range(10):
    lst.append(i)
# general rule: [f(var) for var in iterable]
lst2 = [i for i in range(10)]
print(lst2)

lst3 = []
for i in range(10):
    if i != 5:
        lst.append(i)
# general rule: [f(var) for var in iterable if cond(var)]
lst4 = [i for i in range(10) if i != 5]
print(lst4)

even_lst = [i for i in range(10) if i%2 == 0]
else_lst = [i if i%2 == 0 else None for i in range(10)]


# SET COMPREHENSION
# similar to list comp, but sets can't have duplicate values so content must be hashable
x = {c for c in 'abc'}
y = {c for c in [[1, 2, 3]]}
# y causes error bc the content (list) is not hashable
print(hash(1)) # ok
print(hash([])) #TypeError


# DICT COMPREHENSION
z = ['one', 'two', 'three', 'four', 'five']
new_dict = dict()
for i in z:
    new_dict[i] = len(i)
print(new_dict)
# returns {'one': 3, 'two': 3, 'three': 5, 'four': 4, 'five': 4}

# general rule: {key(var): value(var) for var in iterable if cond(var)}
dict_com = {k: len(k) for k in x}
print(dict_com)
print()


# TUPLE COMPREHENSION
