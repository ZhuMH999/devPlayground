def partial_fractions(top, linear, repeated):
    sub_a = (-1 * linear[1]) / linear[0]
    print(sub_a)
    left_a = sub_values(top, sub_a)
    a = left_a / ((repeated[0] * sub_a + repeated[1]) ** 2)

    sub_c = (-1 * repeated[1]) / repeated[0]
    left_c = sub_values(top, sub_c)
    c = left_c / (linear[0] * sub_c + linear[1])

    sub_b = 10
    left_b = sub_values(top, sub_b) - ((sub_values(repeated, sub_b) ** 2) * a + c * sub_values(linear, sub_b))
    b = left_b / (sub_values(linear, sub_b) * sub_values(repeated, sub_b))
    print(f'a = {a}, b = {b}, c = {c}')

def sub_values(polynomial, value):
    total = 0
    for i in range(len(polynomial)):
        if i == len(polynomial) - 1:
            total += polynomial[i]
        else:
            total += (value ** (len(polynomial) - 1 - i)) * polynomial[i]

    return total

partial_fractions([3, -11, 5], [1, -2], [1, -1])
