def partial_fractions(top, factor1, factor2):
    sub_a = (-1 * factor1[1]) / factor1[0]
    left_a = sub_values(top, sub_a)
    a = left_a / ((factor2[0] * sub_a + factor2[1]) ** 2)

    sub_c = (-1 * factor2[1]) / factor2[0]
    left_c = sub_values(top, sub_c)
    c = left_c / (factor1[0] * sub_c + factor1[1])

    sub_b = 10
    left_b = round(sub_values(top, sub_b) - ((sub_values(factor2, sub_b) ** 2) * a + c * sub_values(factor1, sub_b)), 2)
    b = left_b / (sub_values(factor1, sub_b) * sub_values(factor2, sub_b))
    print(f'a = {a}, b = {b}, c = {c}')

def sub_values(polynomial, value):
    total = 0
    for i in range(len(polynomial)):
        if i == len(polynomial) - 1:
            total += polynomial[i]
        else:
            total += (value ** (len(polynomial) - 1 - i)) * polynomial[i]

    return total

def get_coeff_of_polynomial(string, check_case=False):
    splitted = string.split(')(')
    final = []
    for i in range(len(splitted)):
        term = splitted[i].split('+')
        polynomial = []
        for j in range(len(term)):
            if len(term[j].split('-')) > 1:
                polynomial.append(term[j].split('-')[0].split('x')[0])
                for k in range(len(term[j].split('-')) - 1):
                    polynomial.append('-' + term[j].split('-')[k+1].split('x')[0])
            else:
                polynomial.append(term[j].split('x')[0])
        final.append(polynomial)
    return cleanup_polynomial(final, check_case)

def cleanup_polynomial(string, check_case=False):
    case = 'linear'
    for i in range(len(string)):
        for j in range(len(string[i])):
            if len(string[i][j].split('^')) > 1:
                case = 'repeated'
            if len(string[i][j].split('(')) > 1:
                string[i][j] = string[i][j].split('(')[1].split(')')[0]
            else:
                string[i][j] = string[i][j].split('(')[0].split(')')[0]
            if string[i][j] == '' or string[i][j] == '-':
                string[i][j] += '1'

            string[i][j] = int(string[i][j])
            print(type(string[i][j]))

    if check_case:
        print(string)
        return string, case
    print(string)
    return string, None

numerator, temp = get_coeff_of_polynomial(input('Please enter numerator in the form ax^2+bx+c, with no spaces. >'))
denumerator, temp = get_coeff_of_polynomial(input('Please enter denominator in the form (ax+b)(cx+d)^2 with no spaces >'), True)

print(partial_fractions(numerator[0], denumerator[1], denumerator[0]))
