# [Note]: `iter`is a build-in function. It can be used to build iterator objects,
my_iter = iter([1, 2, 3])
print(my_iter)  # return => <list_iterator object at 0x1030fb080>
# [Note]: `next()` function is used to gradually iterate over their content
print(next(my_iter))  # 1
print(next(my_iter))  # 2
print(next(my_iter))  # 3
# print(next(my_iter)) # error -> [Note]: If there are no more elements, the iterator raises a “StopIteration” exception.


class MyRange:
    def __init__(self, a, b):
        self.a = a
        self.b = b
# [Qns]: self = the memory address of the instance?

    def __iter__(self):
        return self

# [Explaination]: on every call to “next” it moves forward the internal variable “a” and returns its value. When it reaches “b”, it raises the StopIteration exception.
    def __next__(self):
        if self.a < self.b:
            value = self.a
            self.a += 1
            return value
        else:
            raise StopIteration


myRange1 = MyRange(1, 5)
myRange2 = MyRange(1, 5)
# [Note]: Note the diff in memory address
print(myRange1)  # <__main__.MyRange object at 0x1076b3828>
print(myRange2)  # <__main__.MyRange object at 0x10ff25828>

# [Note]: iter() will return the memory address of myRange1. This is the same as print(myRange1)
print(iter(myRange1))  # <__main__.MyRange object at 0x1076b3828>

print(next(myRange1))  # 1
print(next(myRange1))  # 2
print(next(myRange1))
print(next(myRange1))
# print(next(myRange1)) # StopIteration


class SquareRange:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __iter__(self):
        return self

    def __next__(self):
        if self.a < self.b:
            value = self.a
            self.a += 1
            return value**2
        else:
            raise StopIteration


s1 = SquareRange(1, 5)
print(next(s1)) #1
print(next(s1)) #4
