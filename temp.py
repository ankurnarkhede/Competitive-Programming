def fib(n, sum):
    print(n)
    if n < 1:
        return sum
    else:
        return fib(n-1, sum+n)

c = 1000
print(fib(c, 0))