def two_sum(numbers, target):
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return i, j
    return -1, -1


print(two_sum([1, 2, 4], 5))
print(two_sum([1, 2, 4], 7))
