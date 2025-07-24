def partial_fractions(top, factor1, factor2, case):
    sub_a = (-1 * factor1[1]) / factor1[0]
    left_a = sub_values(top, sub_a)
    if case == 'repeated':
        a = left_a / ((factor2[0] * sub_a + factor2[1]) ** 2)
    elif case == 'nonrepeated':
        a = left_a / (factor2[0] * (sub_a ** 2) + factor2[2])
    else:
        a = left_a / (factor2[0] * sub_a + factor2[1])

    if case == 'nonrepeated':  # (x+2)(x^2+0x+1)
        sub_c = 0
        left_c = sub_values(top, sub_c)
        c = (left_c - (a * sub_values(factor2, sub_c))) / (factor1[0] * sub_c + factor1[1])

    else:
        sub_c = (-1 * factor2[1]) / factor2[0]
        left_c = sub_values(top, sub_c)
        c = left_c / (factor1[0] * sub_c + factor1[1])

    if case != 'linear':
        sub_b = check_for_divisable(factor1, factor2, top, a, c, case)
        print(sub_b)
        if case == 'repeated':
            left_b = round(sub_values(top, sub_b) - ((sub_values(factor2, sub_b) ** 2) * a + c * sub_values(factor1, sub_b)), 2)
            b = round(left_b / (sub_values(factor1, sub_b) * sub_values(factor2, sub_b)), 2)

        else:
            left_b = round(sub_values(top, sub_b) - (sub_values(factor2, sub_b) * a + c * sub_values(factor1, sub_b)), 2)
            b = round(left_b / (sub_b * sub_values(factor1, sub_b)), 2)

        print(f'a = {a}, b = {b}, c = {c}, case = {case}')
    else:
        print(f'a = {a}, b = {c}, case = {case}')

def check_for_divisable(factor1, factor2, top, a, c, case):
    stepper = 0
    while True:
        if sub_values(factor1, stepper) != 0 and sub_values(factor2, stepper) != 0:
            if case == 'repeated':
                if round(sub_values(top, stepper) - ((sub_values(factor2, stepper) ** 2) * a + c * sub_values(factor1, stepper)), 2) != 0:
                    return stepper
            elif case == 'nonrepeated':
                if round(sub_values(top, stepper) - (sub_values(factor2, stepper) * a + c * sub_values(factor1, stepper)), 2) != 0:
                    return stepper
        stepper += 1


def sub_values(polynomial, value):
    total = 0
    for i in range(len(polynomial)):
        if i == len(polynomial) - 1:
            total += polynomial[i]
        else:
            total += (value ** (len(polynomial) - 1 - i)) * polynomial[i]

    return total

def get_coeff_of_polynomial(string, check_case=False):
    case = None
    if check_case:
        case = 'linear'
        if ')^' in string:
            case = 'repeated'
        elif '^' in string:
            case = 'nonrepeated'

    splitted = string.split(')(')
    final = []

    for part in splitted:
        part = part.strip()

        part = part.replace('-', '/+-')
        terms = part.split('+')

        polynomial = []
        for term in terms:
            term = term.strip()

            if term == '' or term == '/':
                continue
            if '(' in term:
                term = term.split('(')[-1]
            if ')' in term:
                term = term.split(')')[0]
            if 'x' in term:
                coeff = term.split('x')[0]
                if coeff == '':
                    coeff = '1'
                elif coeff == '-':
                    coeff = '-1'
            else:
                coeff = term
            if coeff == '' or coeff == '-':
                coeff += '1'

            polynomial.append(int(coeff))

        final.append(polynomial)
    return final, case

print('Enter polynomials for the numerator in the form ax^2+bx+c.')
numerator, _ = get_coeff_of_polynomial(input('Please enter the numerator with no spaces. >'))

print('Enter polynomials for the denominator in the forms:\n\nNonrepeated Linear: (ax+b)(cx+d)\nRepeated Linear: (ax+b)(cx+d)^2\nNon-factorisable Quadratic: (ax+b)(cx^2+dx+e)')
denominator, cas = get_coeff_of_polynomial(input('\nPlease enter denominator with no spaces >'), True)

partial_fractions(numerator[0], denominator[0], denominator[1], cas)
