# Uses python3
import sys


def gcd(a, b):
    while b != 0:
        if b > a:
            a, b = b, a
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

