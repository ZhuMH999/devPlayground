"""
Long division of polynomials made in Python by ZhuMH999

To use:
Run the code

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

    if len(remainder) == 0:
        remainder.append(0)

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

def get_polynomials(d):
    while True:
        degree = input(f'Please enter the degree of the {d}. > ')
        if degree.isdigit():
            degree = int(degree)
            break
        print('Sorry. That was not a number. Please input again.')

    e = []
    for i in range(degree + 1):
        while True:
            answer = input(f'Please enter the coefficent of x{str(degree - i).translate(SUP)}. > ')
            if answer.isdigit():
                break
            print('Sorry. That was not a number. Please input again.')
        e.append(int(answer))
    return e

q, r = polynomialDivision(get_polynomials('divisor'), get_polynomials('divident'))
print(f'Quotient = {" ".join(q)}')
print(f'Remainder = {" ".join(r)}')
