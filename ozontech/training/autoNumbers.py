def firstCheck(slice: str):
    if slice[0].isalpha() and slice[1].isdigit() and slice[2].isdigit() and slice[3].isalpha() and slice[4].isalpha():
        return True
    return False

def secondCheck(slice: str):
    if slice[0].isalpha() and slice[1].isdigit() and slice[2].isalpha() and slice[3].isalpha():
        return True
    return False


if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        newStr = str(input())
        result = []
        flag = True

        while len(newStr) >= 4:

            if len(newStr) >= 5 and firstCheck(newStr[:5]):
                result.append(newStr[:5])
                newStr = newStr[5:]

            elif secondCheck(newStr[:4]):
                result.append(newStr[:4])
                newStr = newStr[4:]
            
            else:
                flag = False
                break
        
        if not flag or len(newStr) > 0:
            print("-")
        
        else:
            print(" ".join(result))
