# from collections.abc import Iterable
# 迭代器的原理介绍

class TestIterator(object):
    def __init__(self, x):
        self.x = x
        self.count = 0

    # 只要重写了__iter__方法就是一个可迭代对象
    def __iter__(self):
        return self

    def __next__(self):
        # 每一次for...in都会调用一次__next__方法，获取返回值
        self.count += 1
        if self.count <= self.x:
            return self.count - 1
        else:
            raise StopIteration  # 让迭代器停止


d = TestIterator(10)
# print(isinstance(d, Iterable))
for i in TestIterator(10):
    print(i)
