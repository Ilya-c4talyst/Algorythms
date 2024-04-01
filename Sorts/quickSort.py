def partition(arr, pivot):
    left, center, right = [], [], []
    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            center.append(i)
    return left, center, right


def quickSort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[len(nums) // 2]
    left, center, right = partition(nums, pivot)

    return quickSort(left) + center + quickSort(right)

testCase = [44, 60, 10, 61, 60, 2, 62, 18, 2, 69]
print(quickSort(testCase))