if __name__ == "__main__":
    testCases = int(input())
    lstNums = [[i+"H", i+"S", i+"C", i+"D"] for i in [str(x) for x in range(2, 10)] + ["T", "J", "Q", "K", "A"]]

    dct = {}
    val = 0
    for i in [str(x) for x in range(2, 10)] + ["T", "J", "Q", "K", "A"]:
        dct[i] = lstNums[val]
        val += 1


    def clearDct(iter, dct):
        first, second = iter[0], iter[1]
        dct[first[0]].remove(first)
        dct[second[0]].remove(second)
        return dct
    
    def checkCombo(iter):
        first, second = iter[0], iter[1]
        if first[0] == second[0]:
            return ["A", first[0]]

    for _ in range(testCases):
        players = int(input())
        combinations = []
        iterDct = lstNums.copy()
        me = [str(x) for x in input().split()]
        iterDct = clearDct(me, iterDct)

        for i in range(1, players):


