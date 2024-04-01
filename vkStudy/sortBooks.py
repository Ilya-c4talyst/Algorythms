def merge(a1, a2):
    n1 = len(a1)
    n2 = len(a2)
    i, j = 0, 0
    c = []
    while i < n1 and j < n2:

        if int(a1[i][2]) < int(a2[j][2]):
            c.append(a1[i])
            i += 1

        elif int(a1[i][2]) > int(a2[j][2]):
            c.append(a2[j])
            j += 1
        
        else:
            if a1[i][1] < a2[j][1]:
                c.append(a1[i])
                i += 1
            else:
                c.append(a2[j])
                j += 1

    if a1[i:]:
        for x in range(i, len(a1)):
            c.append(a1[x])

    elif a2[j:]:
        for x in range(j, len(a2)):
            c.append(a2[x])
    return c


def solution(values):

    pivot = len(values) // 2

    a1 = values[:pivot]
    a2 = values[pivot:]

    if len(a1) > 1:
        a1 = solution(a1)
    if len(a2) > 1:
        a2 = solution(a2)
    return merge(a1, a2)


if __name__ == "__main__":
    n = int(input())
    values = []
    for _ in range(n):
        new = [x for x in input().split()]
        st = " ".join(new[1:-1])
        new = [new[0], st, new[-1]]
        values.append(new)
    result = solution(values)
    for i in result:
        print(*i)
