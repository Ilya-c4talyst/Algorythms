nums = [1,1,1,1,2,3,2]

def solution(nums):
    
    for i in range(1, len(nums)):
        current = nums[i]
        if current > 0:
            continue
        j = i - 1
        while j >= 0 and nums[j] > 0:
            nums[j], nums[j+1] = nums[j+1], nums[j]
            j -= 1
        nums[j] = current
    return nums

print(solution(nums))