import time


def timer(func, *args):
    start = time.perf_counter()
    for i in range(1000):
        func(*args)

    return time.perf_counter()-start


print(timer(pow, 2, 1000))
