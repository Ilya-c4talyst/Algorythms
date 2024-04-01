if __name__ == "__main__":
    testcases = int(input())

    for _ in range(testcases):
        # k
        pages = int(input()) 
        depoyed = [str(x) for x in input().split(",")]
        newSet = set()
        for i in depoyed:
            if "-" in i:
                prom = i.split("-")
                for j in range(int(prom[0]), int(prom[1]) + 1):
                    newSet.add(j)
            else:
                newSet.add(int(i))
        
        new = []
        for k in range(1, pages + 1):
            if k not in newSet:
                new.append(int(k))

        afterCheck = []
        stack = []

        for m in range(len(new)):
            if not stack:
                stack.append(new[m])
                continue
            if new[m] == stack[-1] + 1:
                stack.append(new[m])
                continue
            else:
                if len(stack) >= 2:
                    afterCheck.append(f'{stack[0]}-{stack[-1]}')
                else:
                    afterCheck.append(str(stack[-1]))
                stack.clear()
                stack.append(new[m])
        if stack:
            if len(stack) >= 2:
                    afterCheck.append(f'{stack[0]}-{stack[-1]}')
            else:
                afterCheck.append(str(stack[-1]))

        print(", ".join(afterCheck))
            
        

