import time


def fibonacci_1(x):
    if x < 0:
        raise ValueError("x no puede ser menor que 0");
    if x < 2:
        return x
    else:
        actual = 0;
        siguiente = 1;
        for _ in range(x):
            temp = actual + siguiente
            actual = siguiente
            siguiente = temp
        return actual


def fibonacci_2(x):
    if x < 0:
        raise ValueError("x no puede ser menor que 0");
    if x < 2:
        return x
    return fibonacci_2(x - 1) + fibonacci_2(x - 2)


cache = {0: 0, 1: 1}


def fibonacci_3(x):
    if x < 0:
        raise ValueError("x no puede ser menor que 0");
    if x in cache:
        return cache[x]
    else:
        z = fibonacci_3(x - 1) + fibonacci_3(x - 2)
        cache[x] = z
        return z


start_time = time.time()
print(fibonacci_3(9))
print("--- %s seconds ---" % (time.time() - start_time))
