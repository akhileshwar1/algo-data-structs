import time


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


calculated = {}


def dynamic_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n in calculated:
        return calculated[n]
    else:
        calculated[n] = dynamic_fib(n-1) + dynamic_fib(n-2)
        return calculated[n]


def fib_dyn_bottom_up(n):
    lst = [0, 1]
    i = 2
    while i <= n:
        lst.append(lst[i - 1] + lst[i - 2])
        i = i + 1
    return lst[n]


if __name__ == '__main__':
    print(fib(6))
    print(dynamic_fib(100))
    print(fib_dyn_bottom_up(100))
