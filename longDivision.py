"""
Long division of polynomials made in Python by ZhuMH999

To use:
Modify the values in the SQUARE BRACKETS on line 50. DO NOT MODIFY ANYTHING ELSE.
The format is as such: coeffient of highest power, coefficient of second highest power, ... constant of the divident in the first square brackets, then same for the divisor in the second square brackets.
If the power is non existant, put a 0. Include negative signs.

The code can be run in online python IDEs.
"""

import copy

SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

def polynomialDivision(divident, divisor):
    quotient = []
    remainder = copy.deepcopy(divident)
    while len(remainder) >= len(divisor):
        temp = len(remainder) - len(divisor)
        minus_thing = [div * (remainder[0] / divisor[0]) for div in divisor] + temp * [0]
        quotient += [str(remainder[0] / divisor[0])]

        for i in range(len(minus_thing)):
            remainder[i] -= minus_thing[i]

        remainder.pop(0)

    remainder = [str(re) for re in remainder]

    formatted_quotient = format_equation(quotient)
    formatted_remainder = format_equation(remainder)

    return formatted_quotient, formatted_remainder


def format_equation(equation):
    formatted = [equation[i].replace('-', '- ') + f'x{str(len(equation) - 1 - i).translate(SUP)}' for i in range(len(equation))]
    for f in range(len(formatted)):
        if f == len(formatted) - 2:
            formatted[f] = formatted[f][:-1]
        elif f == len(formatted) - 1:
            formatted[f] = formatted[f][:-2]

        if '-' not in formatted[f] and f > 0:
            formatted[f] = '+ ' + formatted[f]
    return formatted


q, r = polynomialDivision([2, 0, -1, 1, 0, -4], [1, -1, -2])
print(f'Quotient = {" ".join(q)}')
print(f'Remainder = {" ".join(r)}')
