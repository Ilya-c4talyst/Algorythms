# import sys


# def solution(nums):
#     stack = []
#     for i in nums:
#         if not i % 2:
#             stack.append(i)
#     if stack:
#         return stack[-1]
#     return -1


# n = input()
# name = sys.stdin.readline().rstrip()
# nums = [int(x) for x in name.split()]
# print(solution(nums))


# def solution(testCase):
#     stack = []
#     new = ""
#     for i in range(len(testCase)):
#         if not stack:
#             stack.append(testCase[i])
#             new += testCase[i]
#             continue
        
#         if testCase[i] == stack[-1]:
#             if testCase[i] != new[-1]:
#                 continue
#             new = new[:-1]
#             stack.pop()
#         else:
#             new += testCase[i]
#             stack.append(testCase[i])
#     return new




# st = input()
# print(solution(st))



# 12
# 100 450 730 800 950 999 1000 3000 3300 8000 9990 10000
# 999

# def solution(nums, target):
#     if len(nums) <= 1:
#         return "false"
#     ind = len(nums) // 2
#     mid = nums[ind]
#     if mid == target:
#         return "true"
#     elif target > mid:
#         return solution(nums[ind:], target)
#     else:
#         return solution(nums[:ind], target)




# n = int(input())
# nums = [int(x) for x in input().split()]
# target = int(input())
# print(solution(nums, target))



# def solution(nums, left, right, maxi):
#     if right > len(nums):
#         return maxi
#     new = 1
#     for i in nums[left:right]:
#         new *= i
#     if new > maxi:
#         maxi = new
#     return solution(nums, left+1, right+1, maxi)
    

# n = input()
# nums = [int(x) for x in input().split()]
# right = int(input())
# left = 0
# maxi = float("-inf")
# print(solution(nums, left, right, maxi))


# def binarMax(nums):
#     ln = len(nums)
#     i = 1
#     while i * 2 <= ln:
#         i = i * 2 + 1
#     return nums[i-1]
    


# n = input()
# nums = [int(x) for x in input().split()]
# print(binarMax(nums))


from collections import defaultdict


n = int(input())
edges = []
for _ in range(n):
    mew = [int(x) for x in input().split()]
    edges.append(mew)

graph = defaultdict(list)

for edge in edges:
    a, b = edge[0], edge[1]
    graph[a].append(b)
    graph[b].append(a)


def has_triangle(graph):
    for u in graph:
        for v in graph[u]:
            for w in graph[v]:
                if w in graph[u]:
                    return True
    return False

# Проверка наличия треугольника
result = has_triangle(graph)
print("Существуют ли три человека, взаимно дружащих друг с другом:", result)

