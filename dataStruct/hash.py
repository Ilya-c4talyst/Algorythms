# def hashTab(st):
#     dct = {}
#     for i in st:
#         dct.setdefault(i, 0)
#         dct[i] += 1
#     x = max(list(dct.values()))
#     return x



# st = input()
# print(hashTab(st))




# def anagram(a, b):
#     dct = {}
#     dct2 = {}
#     for i in a:
#         dct.setdefault(i, 0)
#         dct[i] += 1

#     for j in b:
#         dct2.setdefault(j, 0)
#         dct2[j] += 1

#     for x, h in dct.items():
#         try:
#             if dct2[x] != h:
#                 return "false"
#         except:
#             return "false"
#     return "true"
    
# a, b = map(str, input().split(" "))
# print(anagram(a, b))


def half(nums, target):
    border = 1
    last = len(nums) - 1
    while border < last and nums[border] < target:
        border *= 2
        if nums[border] == target:
            return target
        if border > last:
            border = last
    return [border // 2, border]
    


n = input()
nums = [int(z) for z in input().split()]
target = int(input())
print(*half(nums, target))