# 7/23
# CONTEXT MANAGER
# must have dunder methods __enter__ and __exit__
def __enter__(self):
    return self.file_obj # return the fil object when entering the context
def __exit__(self, exc_type, exc_value, exc_traceback):
    self.file_obj.close() # close the file when exiting the context
    return False # return false to propagate the exception, true to suppress it

# implement index in python -> add __getitem__ method
def __getitem__(self, index):
    return self.line[index] # assume this self.lines is a list of lines
# store by index -> __setitem__
def __setitem__(self, index, value):
    self.line[index] = value
def __delitem__(self, index):
    del self.line[index]
def __contains__(self, item):
    # for i in self.lst:
    #     if i == item:
    #         return True
    # return False
    return item in self.lst



# 7/25
# getitem with non list object
class MyRange:
    def __init__(self, start, end, step):
        self._start = start
        self._end = end
        self._step = step

    def __len__(self):
        return (self._end - self._start) / self._step

    def __getitem__(self, index):
        if type(index) is not int:
            start, stop, step = index.indices(len(self))
            # for using slice: var[start:stop:step]
            # index.indices splits up the values of the index into three
            start_value = self._start + start * self._step
            stop_value = min(self._start + stop * self._step, self._end)
            step_value = step * self._step
        elif index >= 0 or index < len(self):
            return self._start + index * self._step
        else:
            raise IndexError

o = MyRange(0, 10, 2)
# o[2] returns 4



# getattr
class C:
    def __getattr__(self, item):
        print(f'item{item} not found')
        return item + '?'
    # if object is not stored in a class object, it will not be found
    # otherwise, the value stored in the object will be returned

    def __setattr__(self, key, value):
        self.__dict__['_' + key] = value
    # adding an underscore better protects your attributes
    # never pass your setattr, this will not allow you to assign or define vars

o = C()
print(o.aname) # returns itemaname not found\n + aname?
o.aname = 0
print(o.aname) # returns 0
o.b = 2
print(o.b) # this causes can AttributeError since o.b is changes to o._b inside __setattr__



# midterm topics: file reading/writing, space efficiency, operators, iterators, generators,
# overloading, namespace, binding