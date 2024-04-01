



if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        n, p = map(int, input().split())
        littleMoney = 0.00
        for k in range(n):
            newCost = int(input())
            if newCost * p / 100 == int(newCost * p / 100):
                continue
            else:
                littleMoney += newCost * p / 100 - int(newCost * p / 100)
        ans = round(littleMoney, 2)
        if len(str(ans)) == 3:
            print(str(ans) + "0")
        else:
            print(ans)
