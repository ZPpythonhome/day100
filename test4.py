def lazy_sum(*args):
    def sum():
        x=0
        for n in args:
            x=x+n
        return x
    return sum

lazy_sum(1,2,3,4,5,6,7,8,9) #这时候lazy_sum 并没有执行，而是返回一个指向求和的函数的函数名sum 的内存地址。
f=lazy_sum(1,2,3,4,5,6,7,8,9)
print(type(f))
print(f())  # 调用f()函数，才真正调用了 sum 函数进行求和，

