# i = 0
# while i < 5:
#     print(i)
#     i += 1
x = 1

def fact(n):
    if n == 1:
        return n
    else:
        print(f'hello from fact({n})')
        return n * fact(n-1)

# print(fact(5))

# 0 1 1 2 3 5 8 13 ...

# key == n, value == fib(n)
cache = {}

def fib(n):
    if n in cache:
        print('cache hit!')
        return cache[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    # get values
    res1 = fib(n-1)
    res2 = fib(n-2)
    # add to cache
    cache[n-1] = res1
    cache[n-2] = res2
    # return result
    return res1 + res2