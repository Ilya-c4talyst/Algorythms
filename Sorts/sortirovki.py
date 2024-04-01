# quicksort
"""Алгоритм быстрой сортировки"""
# import random

# def quick_sort(a):
#     if len(a) > 1:
#         x = a[random.randint(0, len(a) - 1)]
#         low = [u for u in a if u < x]
#         eq = [u for u in a if u == x]
#         hi = [u for u in a if u > x]
#         a = quick_sort(low) + eq + quick_sort(hi)
#     return a

# if __name__ == "__main__":
#     c = int(input())
#     nums = [int(x) for x in input().split()]
#     print(' '.join([str(x) for x in quick_sort(nums)]))


# """Алгоритм сортировки слиянием."""

# def mergeSort(sort_nums):
#     if len(sort_nums)>1:
#         mid = len(sort_nums)//2
#         lefthalf = sort_nums[:mid]
#         righthalf = sort_nums[mid:]
#         mergeSort(lefthalf)
#         mergeSort(righthalf)
#         i=0
#         j=0
#         k=0
#         while i<len(lefthalf) and j<len(righthalf):
#             if lefthalf[i]<righthalf[j]:
#                 sort_nums[k]=lefthalf[i]
#                 i=i+1
#             else:
#                 sort_nums[k]=righthalf[j]
#                 j=j+1
#             k=k+1
#         while i<len(lefthalf):
#             sort_nums[k]=lefthalf[i]
#             i=i+1
#             k=k+1
#         while j<len(righthalf):
#             sort_nums[k]=righthalf[j]
#             j=j+1
#             k=k+1

# if __name__ == "__main__":
#     c = int(input())
#     nums = [int(x) for x in input().split()]
#     mergeSort(nums)
#     print(' '.join([str(x) for x in nums]))

# """Сортировка вставками"""

# def insertion_sort(array, n):
#   for j in range(n-1):
#     count = 0
#     for i in range(n-1):
#         if array[i] > array[i+1]:
#             new = array[i]
#             array[i] = array[i+1]
#             array[i+1] = new
#             count = 1
#     if count or j == 0:
#       print(' '.join(str(x) for x in array))
#     else:
#        break

# def insertion_sort(nums):
#     for i in range(1, len(nums)):
#         item_to_insert = nums[i]
#         j = i - 1
#         while j >= 0 and nums[j] > item_to_insert:
#             nums[j + 1] = nums[j]
#             j -= 1
#         nums[j + 1] = item_to_insert

# # if __name__ == '__main__':
# #    n = int(input())
# #    numbers = [int(x) for x in input().split()]
# #    insertion_sort(numbers, n)

# def merge(a1, a2):

#     N1, N2 = len(a1), len(a2)
#     i, j = 0, 0
#     c = []

#     while i < N1 and j < N2:
#         if a1[i] < a2[j]:
#             c.append(a1[i])
#             i += 1
#         else:
#             c.append(a2[j])
#             j += 1

#     c += a1[i:] + a2[j:]
#     return c



# def mergeSort(nums):

#     N = len(nums) // 2
#     a1 = nums[:N]
#     a2 = nums[N:]

#     if len(a1) > 1:
#         a1 = mergeSort(a1)
#     if len(a2) > 1:
#         a2 = mergeSort(a2)

#     return merge(a1, a2)


# testData = [1, -1, 0, 3, 2, 8, 0, 1, 6, 89, 10]
# print(mergeSort(testData))

def comb(data):
    gap = len(data)
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.25))
        swaps = False
        for i in range(len(data) - gap):
            j = i + gap
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
                swaps = True
    return data

testData = [1, -1, 0, 3, 2, 8, 0, 1, 6, 89, 10]
print(comb(testData))