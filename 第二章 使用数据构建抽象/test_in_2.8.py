def count(f):  # 装饰函数f，并记录f被调用的次数
    def counted(n):  # 1.定义内部函数counted
        counted.call_count += 1  # 2.每次调用时增加计数器
        return f(n)  # 3.调用原始函数f并返回结果

    counted.call_count = 0  # 4.初始化计数器为0
    return counted  # 5.返回包装后的函数


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


fib = count(fib)
fib(19)
print(fib.call_count)
