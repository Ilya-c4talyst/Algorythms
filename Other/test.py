def divide_polynomials(p, q):
    quot = [0] * (len(p) - len(q) + 1)
    rem = p[:]

    while len(rem) - 1 >= len(q):
        degree = len(rem) - len(q)
        coeff = rem[-1] / q[-1]
        quot[degree] = coeff
        term = [0] * (len(rem) - len(q) + 1)

        for i in range(len(term)):
            term[i] = -q[i] * coeff

        rem = [round(rem[i] + term[i]) for i in range(len(term))]

    return quot, rem

# Пример использования
p = [2, 1, 3, 2]
q = [6, 0, 3]
quotient, remainder = divide_polynomials(p, q)
print("Неполное частное:", quotient)
print("Остаток:", remainder)