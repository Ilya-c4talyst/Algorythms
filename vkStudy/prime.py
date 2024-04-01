def customSort(numbers):
    for i in range(len(numbers)):
        if numbers[i] % 2:
            j = i + 1
            while j < len(numbers):
                if numbers[j] % 2 == 0:
                    numbers[i], numbers[j] = numbers[j], numbers[i]
                    break
                j += 1
    return numbers


if __name__ == "__main__":
    countLst = int(input())
    lstNums = [int(x) for x in input().split()]
    print(*customSort(lstNums))
