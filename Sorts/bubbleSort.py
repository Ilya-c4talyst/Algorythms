nums = [1,7,5,4,3,6,8,0]

def bubbleSort(nums):
    index = 0
    last_index = len(nums) - 1
    swapped = True
    while swapped:
        swapped = False
        while index < last_index:
            if nums[index] > nums[index + 1]:
                swapped = True
                nums[index], nums[index + 1] = nums[index + 1], nums[index]
            index += 1
        index = 0
        last_index -= 1
    return nums
    
print(bubbleSort(nums))
