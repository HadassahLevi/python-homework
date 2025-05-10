
# import time
# def stopwatch(func):
#     def inner(*args):
#         start_time = time.time()
#         result = func(*args)
#         end_time = time.time()
#         print(f"זמן הריצה: {(end_time - start_time) * 1000:.2f} מילישניות")
#         return result
#     return inner



import timeit

def stopwatch(func):
    def inner(*args, **kwargs):
        stmt = f"{func.__name__}(*args, **kwargs)"
        execution_time = timeit.timeit(lambda: func(*args, **kwargs), number=10)
        print(f"זמן הריצה: {(execution_time / 10) * 1000:.2f} מילישניות")
        return func(*args, **kwargs)
    return inner




def cache(func):
    cache_dict = {}
    def inner(*args):
        if args in cache_dict:
            return cache_dict[args]
        result = func(*args)
        cache_dict[args] = result
        return result
    return inner

@stopwatch
@cache
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b

print(fibonacci(1000))
print(fibonacci(10000))
print(fibonacci(10000))


@stopwatch
def fibonacci2(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b
print('*********************')
print(fibonacci2(1000))
print(fibonacci2(10000))

