# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    num, last, current = 0, 0, 0
    stops.insert(0, 0)
    stops.append(distance)
    n = len(stops) - 2
    while current <= n:
        last = current
        while (current <= n) and ((stops[current + 1]-stops[last]) <= tank):
            current = current + 1
        if last == current:
            return -1
        if current <= n:
            num = num + 1
    return num


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
