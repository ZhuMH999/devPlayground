SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

def get_polynomials(d):
    while True:
        degree = input(f'Please enter the degree of the {d}. > ')
        try:
            degree = int(degree)
            break
        except TypeError:
            print('Sorry. That was not a number. Please input again.')

    e = []
    for i in range(degree + 1):
        while True:
            answer = input(f'Please enter the coefficent of x{str(degree - i).translate(SUP)}. > ')
            try:
                answer = int(answer)
                break
            except TypeError:
                print('Sorry. That was not a number. Please input again.')
        e.append(int(answer))
    return e

def sub_in_value(x, eqn):
    total = 0
    for i in range(len(eqn)-1):
        total += eqn[i] * (x ** (len(eqn) - 1 - i))
    total += eqn[-1] * x
    return total


def get_tangent(der, eqn, x, y=None):
    x_coor = x
    if y is None:
        y_coor = sub_in_value(x, eqn)
    else:
        y_coor = y

    gradient = sub_in_value(x_coor, der)
    c = gradient * (-x_coor) + y_coor

    print(f'The tangent is y = {gradient}x + {c}')

get_tangent(get_polynomials('derivative'), get_polynomials('equation'), int(input('Please enter the x value of the point. > ')))
