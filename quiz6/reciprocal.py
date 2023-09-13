import math

numbers = [1, 5 / 2, -6, 0, 0.4, -0.17, 'pi', 3.14, 2-6j, math.pi]
for n in numbers:
    try:
        reciprocal = 1 / n
        print(f"The reciprocal of {n} is {round(reciprocal, 2)}")
    except ZeroDivisionError:
        print('division by zero')
    except TypeError as te:
        if isinstance(n, complex):
            print("type complex doesn't define __round__ method")
        if isinstance(n, str):
            print("unsupported operand type(s) for /: 'int' and 'str'")
