def merge(a, b):
    N1 = len(a)
    N2 = len(b)
    i = j = 0

    c = []

    while i < N1 and j < N2:
        if a[i] <=b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    
    return c + a[i:] + b[j:]


def mergeSort(nums):
    val = len(nums) // 2
    a1 = nums[:val]
    a2 = nums[val:]

    if len(a1) > 1:
        a1 = mergeSort(a1)
    if len(a2) > 1:
        a2 = mergeSort(a2)
    
    return merge(a1, a2)

n = int(input())
nums = [int(x) for x in input().split()]
print(mergeSort(nums))

