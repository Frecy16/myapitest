import time


def cal_time(fn):
    print('我是外部函数，我被调用了')
    print('fn = {}'.format(fn))
    def inner(x):
        start = time.time()
        fn(x)
        end = time.time()
        print('代码耗时', end - start)
    return inner

@cal_time # 第一件事调用cal_time;第二件事把被装饰的函数传递给fn
def demo(n):
    x = 0
    for i in range(1, n):
        x += 1
    print(x)

# 第三件事：当再次调用demo函数时，此时的demo函数已经不再试上面的demo，而是装饰函数cal_time的返回值，也就是inner函数
print('装饰后的demo = {}'.format(demo))
demo(100000000)