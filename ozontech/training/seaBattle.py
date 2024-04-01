if __name__ == "__main__":
    n = int(input())
    ships = [[int(x) for x in input().split()] for _ in range(n)]
    rightPlace = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
    for current in ships:
        current.sort()
        if current == rightPlace:
            print("YES")
        else:
            print("NO")