# L R U D B E N

if __name__ == "__main__":
    cases = int(input())
    for _ in range(cases):
        newCase = str(input()).strip()
        start = [[]]
        now_x, now_y = 0, 0
        for i in newCase:


            if i == "R":
                if now_x == len(start[now_y]):
                    continue
                now_x += 1

            elif i == "L":
                if now_x == 0:
                    continue
                now_x -= 1

            elif i == "U":
                if now_y == 0:
                    continue
                now_y -= 1
                if start[now_y] == []:
                    now_x = 0
                elif now_x > len(start[now_y]):
                    now_x = len(start[now_y])

            elif i == "D":
                if now_y == len(start) - 1:
                    continue
                now_y += 1
                if start[now_y] == []:
                    now_x = 0
                elif now_x > len(start[now_y]):
                    now_x = len(start[now_y])

            elif i == "B":
                now_x = 0


            elif i == "E":
                now_x = len(start[now_y])

            elif i == "N":
                toReplace = start[now_y][now_x:]
                start[now_y] = start[now_y][:now_x]
                new = start[:now_y + 1]
                end = start[now_y + 1:]
                if toReplace:
                    new.append(toReplace)
                if not toReplace:
                    new.append([])
                for a in end:
                    new.append(a)
                start = new
                now_y += 1
                now_x = 0

            else:
                if now_x < len(start[now_y]):
                    start[now_y] = start[now_y][:now_x] + [i] + start[now_y][now_x:]
                else:
                    start[now_y].append(i)
                now_x += 1



        for x in range(len(start)):
            if start[x]:
                print(''.join(start[x]).strip())
            else:
                print("")
        print("-")