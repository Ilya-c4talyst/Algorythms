if __name__ == "__main__":
    daysPerMonth = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    n = int(input())
    for _ in range(n):
        date, month, year = map(int, input().split())
        if month == 2:
            if (year % 4 == 0 and year % 100) or year % 400 == 0:
                if date <= daysPerMonth[1] + 1:
                    print("YES")
                else:
                    print("NO")
                continue
        if date <= daysPerMonth[month-1]:
            print("YES")
        else:
            print("NO")
