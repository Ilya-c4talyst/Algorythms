# def find_two_indexes(data, expected_sum):
#     # Ваше решение?
#     i = 0
#     while data[i] <= expected_sum:
#         testCase = data[i]
#         if expected_sum - testCase in data:
#             k = data.index(expected_sum - testCase)
#             return (i, k)
#         i += 1
#     return None


# if __name__ == '__main__':
#     data = [1, 2, 3, 4, 5, 6, 7, 11]
#     expected_sum = 10
#     print(find_two_indexes(data, expected_sum))

def find_two_indexes(data, expected_result):
    left_pointer = 0
    right_pointer = len(data) - 1
    while left_pointer < right_pointer:
        newSum = data[left_pointer] + data[right_pointer]
        if newSum == expected_result:
            return left_pointer, right_pointer
        if newSum < expected_result:
            left_pointer += 1
            continue
        else:
            right_pointer -= 1
            continue
    return None
        


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 11]
    expected_result = 10
    print(find_two_indexes(data, expected_result))