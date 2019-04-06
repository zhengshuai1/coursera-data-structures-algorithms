# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    index1 = n-1
    for i in range(n):
        if (index1 == n-1) | (numbers[i] > numbers[index1]):
            index1 = i
    index2 = n-1
    for j in range(n):
        if (j != index1) & ((index2 == n-1) | (numbers[j] > numbers[index2])):
            index2 = j
    return numbers[index1] * numbers[index2]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
