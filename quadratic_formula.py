import cmath


def quadratic_formula(a, b, c):

    if a == 0:
        raise ValueError("二次式ではありません")

    elif b**2 - 4 * a * c == 0:
        x = -b / (2*a)
        return x

    else:
        x1 = (-b - cmath.sqrt(b**2 - 4 * a * c)) / (2*a)
        x2 = (-b + cmath.sqrt(b**2 - 4 * a * c)) / (2*a)
        return x1, x2


# (1)
print(f"(1)の答えは、{quadratic_formula(1, -6, 9)}")
# (2)
print(f"(2)の答えは、{quadratic_formula(1, 2, -8)}")
# (3)
print(f"(3)の答えは、{quadratic_formula(8, -6, -35)}")
# (4)
print(f"(4)の答えは、{quadratic_formula(1, 0, 1)}")
