def solution(digits):
    L = {
            '2':"abc",'3':"def",'4':"ghi",'5':"jkl",
            '6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"
        }
    ln, res = len(digits), []
    if digits == "": return []
    def recurs(position, val):
        if position == ln: res.append(val)
        else:
            letters = L[digits[position]]
            for i in letters:
                recurs(position+1, val+i)
    recurs(0, "")
    return res
print(solution("23"))
    