
# 迭代器是一个对象，定义class
# 生成器写法上像一个函数
def my_gen(n):
    i = 0
    while i < n:
        # return i  # 函数里的return表示函数的执行结果
        yield i  # yield关键字，将函数变成生成器
        i += 1

G = my_gen(10)
for i in G:
    print(i)
# print(next(iter(G)))
# print(next(iter(G)))
# print(next(iter(G)))