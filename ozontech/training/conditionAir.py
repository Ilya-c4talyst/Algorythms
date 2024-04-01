if __name__ == "__main__":
    cases = int(input())
    for _ in range(cases):
        start = [15, 30]
        n = int(input())

        for i in range(n):
            digit, value = map(str, input().split())

            if digit == "<=":
                start[1] = min(int(value), start[1])
            else:
                start[0] = max(int(value), start[0])
            
            if start[1] - start[0] >= 0 and start[0] >= 15 and start[0] <= 30:
                print(start[0])
            else:
                print(-1)
        print("")
