def interpolSearch(data, value):
    left = 0
    right = len(data) - 1
    while data[left] < value < data[right]:
        if data[left] == data[right]:
            break
        index = left + (right - left) * (value - data[left]) // (data[right] - data[left])
        if data[index] > value:
            right = index - 1
        elif data[index] < value:
            left = index + 1
        else:
            return index

    if data[left] == value:
        return left
    if data[right] == value:
        return right
    return left

n = input()
testCase = [int(x) for x in input().split()]
value = int(input())
print(interpolSearch(testCase, value)) 