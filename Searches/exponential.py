def binarySearch():
    pass


def half(nums, target):
    border = 1
    last = len(nums) - 1
    while border < last and nums[border] < target:
        border *= 2
        if nums[border] == target:
            return target
        if border > last:
            border = last
    return binarySearch(nums, target, border // 2, border)