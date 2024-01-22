"""Darts"""
# def solution(lstValues: list) -> int:
#     points = 0
#     for i in range(3):
#         maxOut = max(lstValues[i])
#         if maxOut <= 0.1:
#             points += 3
#         elif maxOut <= 0.8:
#             points += 2
#         elif maxOut <= 1:
#             points += 1
#     return points


# if __name__ == "__main__":
#     first = [float(x) for x in input().split()]
#     second = [float(x) for x in input().split()]
#     third = [float(x) for x in input().split()]
#     print(solution([first, second, third]))


"""Text"""
# def solution(text: str) -> list:
#     lstText = text.split("#")

#     if len(lstText) < 2:
#         return [len(lstText[0]), len(lstText[0])]

#     lstText = sorted(lstText, key=lambda x: len(x))
#     return [len(lstText[0]), len(lstText[-1])]


# if __name__ == "__main__":
#     stLenght = int(input())
#     text = str(input())
#     print(*solution(text))


"""Bridge"""
# def check_square(h: float, levels: list) -> float:
#     upper_area = 0
#     lower_area = 0
    
#     for i in range(len(levels) - 1):
#         upper_area += max(0, h - levels[i])
#         lower_area += max(0, levels[i+1] - h)

#     return upper_area - lower_area


# def solution(levels: list) -> float:
#     left, right = min(levels), max(levels)
#     zero = 1e-9
    
#     while abs(right - left) > zero:
#         mid = (left + right) / 2

#         if check_square(mid, levels) >= 0:
#             right = mid
#         else:
#             left = mid
            
#     return round((left + right) / 2, 6)


# if __name__ == "__main__":
#     n = int(input())
#     levels = list(map(int, input().split()))

#     print(solution(levels))


"""Books"""
# def solution(values: list) -> list:
#     setValues = set(values)
#     result = []
#     stack = []

#     for i in setValues:

#         if not stack:
#             result.append(str(i))
#             stack.append(i)
#             continue

#         if i - stack[-1] != 1:
#             if len(stack) == 2:
#                 result.append(str(stack[1]))
#             elif len(stack) > 2:
#                 result.append("...")
#                 result.append(str(stack[-1]))
#             result.append(str(i))
#             stack.clear()
#             stack.append(i)

#         else:
#             stack.append(i)

#     if stack and len(stack) == 2:
#         result.append(str(stack[1]))
#     elif stack and len(stack) > 1:
#         result.append("...")
#         result.append(str(stack[-1]))

#     return result


# if __name__ == "__main__":
#     ctValues = int(input())
#     values = (int(x) for x in input().split())
#     print(' '.join(solution(values)))


"""Ozon"""
# from collections import defaultdict

# def solution(cars: list, path: list) -> int:
#     graph = defaultdict(list)

#     for u, car_num, v in cars:
#         graph[u].append((v, car_num))
#         graph[v].append((u, car_num))

#     current = 1
#     for car_num in path:
#         found = False
#         for neighbor, neighbor_car_num in graph[current]:
#             if neighbor_car_num == car_num:
#                 current = neighbor
#                 found = True
#                 break

#         if not found:
#             return 0

#     return current


# if __name__ == "__main__":
#     n, m, k = map(int, input().split())
#     cars = [tuple(map(int, input().split())) for _ in range(m)]
#     path = list(map(int, input().split()))
#     print(solution(cars, path))


