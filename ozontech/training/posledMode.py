if __name__ == "__main__":
    cases = int(input())
    for _ in range(cases):
        lenght = int(input())
        numsFirst = [int(x) for x in input().split()]
        numsSecond = []
        start = []
        flag = None
        for i in range(lenght):
            if not start:
                start.append(numsFirst[i])
                continue
            if numsFirst[i] - start[-1] == 1 and (flag is True or flag is None):
                flag = True 
                start.append(numsFirst[i])
            elif numsFirst[i] - start[-1] == -1 and (flag is False or flag is None):
                flag = False
                start.append(numsFirst[i])
            else:
                if flag is True:
                    mnozh = len(start) - 1
                elif flag == False:
                    mnozh = -(len(start) - 1)
                else:
                    mnozh = 0
                numsSecond.append(start[0])
                numsSecond.append(mnozh)
                start, flag = [numsFirst[i]], None
        if start:
            if flag is True:
                mnozh = len(start) - 1
            elif flag == False:
                mnozh = -(len(start) - 1)
            else:
                mnozh = 0
            numsSecond.append(start[0])
            numsSecond.append(mnozh)
        print(len(numsSecond))
        print(*numsSecond)

