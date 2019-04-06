# Uses python3
import time
def calc_fib(n):
    if (n <= 1):
        return n
    else:
        a, b = 0, 1
        for i in range(1, n):
            a, b = b, a+b
    return b

n = int(input())
t1 = time.time()
print(calc_fib(n))
t2 = time.time()
print("the run time is {:.4f}".format(t2-t1))