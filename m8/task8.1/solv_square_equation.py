import sys


def validate_param(counter=0, len_arg=0):
    if counter == 3:
        print('You have exceeded the maximum number of attempts')
        exit(0)
    try:
        if len_arg >= 4:
            numbers = [int(arg) for arg in sys.argv[1:4]]
        else:
            print("Please, enter a, b, c separated by a space: ")
            numbers = [int(i) for i in input().split()]
        return numbers
    except ValueError:
        print('Value Error!')
        return validate_param(counter + 1)


def discriminant(a, b, c):
    d = (b ** 2) - 4 * (a * c)
    if d > 0:
        return d
    return None


def roots(d, a, b, c):
    if d is None:
        return [None, None]
    elif d == 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        return [x1, None]
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return [x1, x2]


def solv_square(a, b, c):
    d = discriminant(a, b, c)
    x1, x2 = roots(d, a, b, c)
    return [x1, x2]


def square_print(a, b, c, *roots):
    print(f'''a = {a}, b = {b}, c = {c}
Roots of the equation are: {roots}''')


def main():
    len_arg = len(sys.argv)
    a, b, c = validate_param(len_arg=len_arg)
    x1, x2 = solv_square(a, b, c)
    square_print(a, b, c, x1, x2)


if __name__ == "__main__":
    main()