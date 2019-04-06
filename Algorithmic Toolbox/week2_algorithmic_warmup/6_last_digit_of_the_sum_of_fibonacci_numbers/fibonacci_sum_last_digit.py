# Uses python3
import sys


def calc_fib(n):
    if (n <= 1):
        return n
    else:
        a, b = 0, 1
        for i in range(1, n):
            a, b = b, a+b
    return b


def fibonacci_sum(n):
    if n <= 1:
        return n
    sum = 0
    if n % 3 == 0:
        for i in range(1, n+1):
            if i % 3 == 0:
                sum = sum % 10 + calc_fib(i) % 10
        return (2 * sum) % 10
    elif n % 3 == 1:
        for i in range(1, n + 1):
            if i % 3 == 0:
                sum = sum % 10 + calc_fib(i) % 10
        return (2 * sum % 10 + calc_fib(n) % 10) % 10
    elif n % 3 == 2:
        for i in range(1, n + 1):
            if i % 3 == 0:
                sum = sum % 10 + calc_fib(i) % 10
        return (2 * sum % 10 + calc_fib(n) % 10 + calc_fib(n-1) % 10) % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n))
