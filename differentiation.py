import copy

SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

def get_coeff_of_polynomial(string):
    try:
        final = []

        s = string
        s = s.strip()

        s = s.replace('-', '/+-')
        terms = s.split('+')

        for term in terms:
            polynomial = []
            term = term.strip('/')

            if term == '' or term == '/':
                continue
            if 'x' in term:
                coeff = term.split('x')[0]
            else:
                coeff = term
            if coeff == '' or coeff == '-':
                coeff += '1'

            exponent = 0
            if '^' in term:
                exponent = term.split('^')[1]
                if 'n' in exponent:
                    exponent = '-' + term.split('n')[1]
            elif '^' not in term and 'x' in term:
                exponent = 1

            polynomial.extend((int(coeff), int(exponent)))

            final.append(polynomial)
        return final
    except:
        print('That was not a valid polynomial. Please restart code and enter again.')
        exit()

def get_number_input(inpt):
    tested = False
    while not tested:
        try:
            number = int(input(inpt))
            tested = True
        except ValueError:
            print('That was not a number. Please try again. ')
    return number

def sub_in_value(x, eqn):
    total = 0
    for i in range(len(eqn)):
        total += eqn[i][0] * (x ** eqn[i][1])
    return total

def get_derivative(eqn):
    der = copy.deepcopy(eqn)
    for term in der:
        if term[1] != 0:
            term[0] *= term[1]
            term[1] -= 1
        else:
            term[0] = 0
    return der

def get_tangent_and_normal(eqn, x):
    der = get_derivative(eqn)

    x_coor = x
    y_coor = sub_in_value(x_coor, eqn)

    gradient = sub_in_value(x_coor, der)
    c = gradient * (-x_coor) + y_coor

    print(f'The tangent is y = {gradient}x + {c}')

    if gradient == 0:
        print(f'The normal is x = {x_coor}')
    else:
        gradient_normal = -1 / gradient
        c_normal = y_coor - gradient_normal * x_coor
        print(f'The normal is y = {gradient_normal}x + {c_normal}.')


print('Enter polynomial to differentiate in the form ax^2+bx+c.\nFor negative powers, please express it in the form x^n3, where n substitutes the negative sign.')
fx = get_coeff_of_polynomial(input('Please enter the polynomial with no spaces. >'))

xcoor = get_number_input('Please enter the value of x for which you want the tangent to lie on. > ')

get_tangent_and_normal(fx, xcoor)
