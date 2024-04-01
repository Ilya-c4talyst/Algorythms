def binarSearch(nums: list, target: int) -> int:
    right = len(nums) - 1
    left = 0
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid -1

    return -1

nums = [1, 2, 5, 8, 12, 12, 13, 20, 22, 23, 24, 30, 32]
target = 12
print(binarSearch(nums, target))