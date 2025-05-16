import copy

def polynomialDivision(divident, divisor):
    quotient = []
    remainder = copy.deepcopy(divident)
    while len(remainder) >= len(divisor):
        temp = len(remainder) - len(divisor)
        minus_thing = [div * (remainder[0] / divisor[0]) for div in divisor] + temp * [0]
        quotient += [remainder[0] / divisor[0]]

        for i in range(len(minus_thing)):
            remainder[i] -= minus_thing[i]

        remainder.pop(0)

    formatted_quotient = [str(quotient[i]) + f'x^{len(quotient) - 1 - i}' for i in range(len(quotient))]
    formatted_remainder = [str(remainder[i]) + f'x^{len(remainder) - 1 - i}' for i in range(len(remainder))]

    return formatted_quotient, formatted_remainder


q, r = polynomialDivision([1, -10, 27, -46, 28], [1, -7])
print(f'Quotient = {" ".join(q)}')
print(f'Remainder = {" ".join(r)}')
