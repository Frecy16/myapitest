def fibonacci(n):
    num1, num2 = 0, 1
    count = 0
    while count <= n - 1:
        x = num1
        num1, num2 = num2, num1 + num2
        count += 1
        yield x

F = fibonacci(13)
for i in F:
    print(i)