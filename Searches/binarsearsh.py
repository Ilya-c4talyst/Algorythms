def binarSearch(nums, target, left, right):
    if left > right:
        return
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    if target < nums[mid]:
        return binarSearch(nums, target, left, mid - 1)
    else:
        return binarSearch(nums, target, mid + 1, right) 


nums = [1, 2, 5, 8, 12, 12, 13, 20, 22, 23, 24, 30, 32]
target = 12
print(binarSearch(nums, target, 0, len(nums)-1))


wins = [1223125, 2128437, 2128500, 2741001, 4567687, 4567890, 7495938, 9314543]
my_ticket = 4567890


def find_element(sorted_numbers, element):
    """Находит индекс element в отсортированном списке sorted_numbers."""
    left = 0
    right = len(sorted_numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_numbers[mid] == element:
            return mid
        if sorted_numbers[mid] < element:
            left = mid + 1
        else:
            right = mid - 1
    return None


print(find_element(wins, my_ticket))